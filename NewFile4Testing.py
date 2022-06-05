with open("NewFile4Testing.rtf", "r+") as f:
        for i in f:
            #importing Path class.
            from pathlib import Path
    
  
    #
    #
            def replacetext(search_text, replace_text):
  
    # 
                file = Path("NewFile4Testing.rtf")
  
    # 
    # 
                data = file.read_text()
  
    # 
                data = data.replace(search_text, replace_text)
    # 
    # 
                file.write_text(data)
  
    # 
        # 
        # 
                search_text = "python"
        #
        #
                replace_text = "\n"
#
#
                print(replacetext(search_text, replace_text))