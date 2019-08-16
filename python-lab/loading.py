import time, sys, os, math, random

basic = ['|','/','-','\\']
simple_dots = ['⠋','⠙','⠹','⠸','⠼','⠴','⠦','⠧','⠇','⠏']
more_dots=["⢀⠀","⡀⠀","⠄⠀","⢂⠀","⡂⠀","⠅⠀","⢃⠀","⡃⠀","⠍⠀","⢋⠀","⡋⠀","⠍⠁","⢋⠁","⡋⠁","⠍⠉","⠋⠉","⠋⠉","⠉⠙","⠉⠙","⠉⠩","⠈⢙","⠈⡙","⢈⠩","⡀⢙","⠄⡙","⢂⠩","⡂⢘","⠅⡘","⢃⠨","⡃⢐","⠍⡐","⢋⠠","⡋⢀","⠍⡁","⢋⠁","⡋⠁","⠍⠉","⠋⠉","⠋⠉","⠉⠙","⠉⠙","⠉⠩","⠈⢙","⠈⡙","⠈⠩","⠀⢙","⠀⡙","⠀⠩","⠀⢘","⠀⡘","⠀⠨","⠀⢐","⠀⡐","⠀⠠","⠀⢀","⠀⡀"]
horizontal_bar=["▏","▎","▍","▌","▋","▊","▉","▊","▋","▌","▍","▎"]
vertical_bar=["▁","▃","▄","▅","▆","▇","▆","▅","▄","▃"]
star=["✶ ","✸ ","✹ ","✺ ","✹ ","✷ "]
boxBounce = ["▖","▘","▝","▗"]
arrow= ["← ","↖ ","↑ ","↗ ","→ ","↘ ","↓ ","↙ "]
right_direction = ["▹▹▹▹▹","▸▹▹▹▹","▹▸▹▹▹","▹▹▸▹▹","▹▹▹▸▹","▹▹▹▹▸"]

def show_loader(loading,sec=None):
    os.system('setterm -cursor off')
    itr = 0
    for i in range(1,int(sec)*10):
        c = "\r{}s Loading {}".format(math.ceil(i/10),loading[i%len(loading)])
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

if __name__ == '__main__':
    loader_type = ""
    print("This is a loading Program.\nYou can see your favourite terminal Loader for as long as you like")

    while True:
        print("Enter the Loader Type\n")
        loader_type = input("1. Basic\n2. Simple Dots\n3. More Dots\n4. Horizontal Bar\n5. Vertical Bar\n6. Star\n7. Box Bounce\n8. Arrow\n9. Right Direction\n10. Exit\nEnter the Choice Number\t")
        if loader_type == '10':
            print("Thank you for your interest")
            break
        sec = input("Enter the number of seconds you want to see the loader\t")

        loader_dict = {
            '1': basic,
            '2':simple_dots, 
            '3':more_dots, 
            '4':horizontal_bar, 
            '5':vertical_bar, 
            '6':star, 
            '7':boxBounce, 
            '8':arrow,
            '9':right_direction
        }
        t_end = time.time() + int(sec)

        # show_loader(random.choice([loading,loading2]),sec)
        show_loader(loader_dict.get(loader_type,basic),sec)

        sys.stdout.write('\n')
        sys.stdout.flush()
        os.system('setterm -cursor on')
