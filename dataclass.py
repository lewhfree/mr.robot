class Data:
    def __init__(self, prompt: str, res: str, children: list = None):
        self.prompt = prompt
        self.res = res
        self.children = children if children is not None else []

    def __str__(self):
        return "class stores prompt, res, children"

    def toDict(self):
        """
            This should help facilitate long term storage because you could store the tree as a json file probably
        """
        
        return {
            "prompt": self.prompt,
            "result": self.res,
            "children": [child.toDict() for child in self.children]
        }
