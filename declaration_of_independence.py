string = "When in the Course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation. We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.--That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed, --That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to institute new Government, laying its foundation on such principles and organizing its powers in such form, as to them shall seem most likely to effect their Safety and Happiness. Prudence, indeed, will dictate that Governments long established should not be changed for light and transient causes; and accordingly all experience hath shewn, that mankind are more disposed to suffer, while evils are sufferable, than to right themselves by abolishing the forms to which they are accustomed. But when a long train of abuses and usurpations, pursuing invariably the same Object evinces a design to reduce them under absolute Despotism, it is their right, it is their duty, to throw off such Government, and to provide new Guards for their future security.--Such has been the patient sufferance of these Colonies; and such is now the necessity which constrains them to alter their former Systems of Government. The history of the present King of Great Britain is a history of repeated injuries and usurpations, all having in direct object the establishment of an absolute Tyranny over these States. To prove this, let Facts be submitted to a candid world."

write = input("Enter d for declaration of independence, and anything else to write your own: ")

limit = int(input("Enter the maximum length of what you would consider a 'small' word: "))

if write != "d":
    print()
    string = input("Enter a string: ")
    print()
else:
    print()
    
words = string.split(" ")

large = 0
small = 0
for i in words:
    if len(i) > limit:
        large += 1
    else:
        small += 1

percent_large = (large / len(words))* 100
percent_small = (small / len(words))* 100

print(format(percent_large, ".2f"), "% large words (greater than ",limit, " letters)", sep = "")
print(format(percent_small, ".2f"), "% small words ( greater than ", limit, " letters)",sep = "")
print()
print("In the graphical representation, large words will be represented in red and small words will be represented in green.")

import turtle

turtle.setup(500,500)
turtle.up()
turtle.pensize(5)

x = -225
y = 225

for i in words:
    if x > 225:
        x = -225
        y -= 25
    if len(i) > limit:
        turtle.goto(x,y)
        turtle.color("red")
        turtle.down()
        turtle.goto(x+1,y+1)
        turtle.up()
        x += 5
        turtle.goto(x,y)
    else:
        turtle.goto(x,y)
        turtle.color("green")
        turtle.down()
        turtle.goto(x+1,y+1)
        turtle.up()
        x += 5
        turtle.goto(x,y)
        
        
