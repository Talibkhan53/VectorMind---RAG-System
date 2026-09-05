class ContextBuilder:
    def build(self,result):
        context = []
        for chunk,score in result:
            context.append(chunk)
        return "\n---\n".join(context)  
