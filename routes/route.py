from fastapi import APIRouter, HTTPException
from models.blogs import Blog
from config.database import collection_name
from schema.schemas import individual_serial,list_serial
from bson import ObjectId

router = APIRouter()

# GET Request
@router.get("/blogs")
async def get_all_blogs():
    blogs = list_serial(collection_name.find())
    return blogs

# POST Request
@router.post("/blogs/")
async def post_blog(blog: Blog):
    blog_id = collection_name.insert_one(dict(blog)).inserted_id
    return {"id": str(blog_id), **blog.dict()}

@router.put("/{id}")
async def update_blog(id:str, blog: Blog):
    updated_post = collection_name.update_one({"_id": ObjectId(id)}, {"$set": dict(blog)})
    #find one and update or update one?
    if updated_post.modified_count == 1:
        return {"message": "Post updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Post not found")

@router.put("/{id}/like")
async def like_blog(id: str):
    post = collection_name.find_one({"_id": ObjectId(id)})
    post["likes"] = post["likes"] + 1  # Initialize and increment likes count

    # Update the likes
    collection_name.update_one({"_id": id}, {"$set": dict(post)})

    return {"message": "Post liked successfully!"}

@router.put("/{id}/dislike")
async def like_blog(id: str):
    post = collection_name.find_one({"_id": ObjectId(id)})
    post["dislikes"] = post["dislikes"] + 1  # Initialize and increment likes count

    # Update the likes
    collection_name.update_one({"_id": ObjectId(id)}, {"$set": dict(post)})

    return {"message": "Post disliked successfully!"}

@router.put("/{id}/comment")
async def like_blog(id: str, comment):
    post = collection_name.find_one({"_id": ObjectId(id)})
    post['comment'] = comment
    # Update the likes
    collection_name.update_one({"_id": ObjectId(id)}, {"$set": dict(post)})

    return {"message": "Commented successfully"}

@router.delete("/{id}")
async def delete_blog(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})