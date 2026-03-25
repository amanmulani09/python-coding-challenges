class Example:
    
    def replace_smiley(_self_,text:str) -> str:
        if len(text) < 1 or not isinstance(text, str):
            return ''
        return text.replace(":)","😊")

print(Example().replace_smiley("Hello :) How are you :) ?"))