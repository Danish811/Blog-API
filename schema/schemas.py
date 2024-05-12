
def individual_serial(Blog):
    return {
        "id": str(Blog["_id"]),
        "name": str(Blog["name"]),
        "likes": str(Blog["likes"]),
        "dislikes": str(Blog["dislikes"]),
        "blog_content": str(Blog["content"]),
        "comments": str(Blog["comments"])
    }

def list_serial(Blogs) :
    return [individual_serial(Blog) for Blog in Blogs]