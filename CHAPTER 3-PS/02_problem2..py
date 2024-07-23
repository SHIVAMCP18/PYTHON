letter = ''' Dear <|Name|>
    You are selected!
    <|Date|> '''

print(letter.replace("<|Name|>" , "shivam").replace("<|Date|>" , "18 sept 2030"))
