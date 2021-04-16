print('''
                                    ..,,,..
                             ..,,;;;;;;;;;;;;;,.            
                           '"     ;;;;;;;;';;;;;;,.          
                       .   ,  -'";.  ;;;;;;;';" ';;;,
                      '  -' ';';; ;;   ;;;;;;'     "";,
                   . "   ,;;,';,'; ;;   ;;;;;, ,;,_   ;,.'
                  ;    ;";;;"        ";, """:;;;"';;;  ' ,
                 ;   ;' ;"'            ;;,;;,  .;; ;;;   ,,,
                ;   ' ;;"               ;;;;;; ;;;  ;; ,;;;
                  , ;; ;                " ;;;; ';',;;  ;;;
               . ,' ;;;;                  ";;;, ; ;;'  ';;;
                 , ,;';;                 ''";;;   ";    ';;;;
              , ;  ;  ;;         _.,,     ' ";;, ,;;., ,;;;;;;
             ,  ;, ;, ;;'"-    =" _,."'-   ' ;;;,;;;;;   ;;;;;;,
            ,  ,;; '; .'"(o     .'(O)"-    ' ';;;;;;,  ,;;;;" ;;;
       ' ,,    ;; ,;' ;;-"'      '   '    '  ;;;;;; ;   ';;;  ';;;
             ,;;  ;'                      '  ;; ;;';   ,;;;    ;;'
            ;;;   ;,   '  .'               ' ';;;;  ,;;; ;;  ,;;;
          ,;;'    ';  ;;. '- = .'             ;;"; ;;;;'  "  ';;  ,
          ;;   ,; '  ,;';   . _               ;; ' ;;;; .;  ,'" ,;;
         ,;;  ;;;,   ;;,;;."_"_"=            ,;;  ,;;;;.;;,    ;;;'
       ,''  ,;;;;;   ;;; ; ;," ,'            ;;' ;  ';;;;;;;,   ;'
         .,;;;'      ;;; ;;  ""    .-""""''  ;; ;  ,;;";";;;;;,  ',
        ;;;'        ;;; ,;;;._  .-"           ; ;,;;;' ;,';;;;;;;, '
        ;;        .;;  ,;;;;;;;;"              ; ,;;'  ';  ";;;;;;;,
         ;;      ;;   ,;;;;;;;;;'               ; ;' ;;;    ';;;;;;;;;
          ;      ;;   ;;"';;;;;;                  ;;, ;;;;;   ;;;;;;;;;
           '      ;;  ;;   ";;"                   ';;;';;"' ,;;;;,;;;
                  ;;, ';    .                      ';;;,.' ,;;;;,;;;
                 ,;;; ;'  .'                   '   ,;;;;;, ;;;;,;;;
            ;, ,;;;' ,' .'                     '  ;;;;;;;; ;;;;;,;;;
            ';;;'     .'      .                .  ';;;;;;   ;;;;;,;;;,

''')
print("Welcome to The Console Makeout.")
print("Your wife is stressed. Your mission is to calm your partner.")

ques_1 = input(
    "Your wife is not talking to you.\n What do you do?\n A. Approach your partner.\n B. Stay where you're.\n Choose A or B ")

ques_1l = ques_1.lower()
if ques_1l == "a":
    ques_2 = input(
        "\nShe is telling what's bothering Her.\n What do you do?\n A. Listen....\n B. Interrupt Her\n Choose A or B ")
    ques_2l = ques_2.lower()

    if ques_2l == "a":
        ques_3 = input(
            "\nShe is telling what should've happen rather than a certain thing.\n What do you do?\n A. Pacify Her....\n B. Interrupt Her\n Choose A or B ")
        ques_3l = ques_3.lower()

        if ques_3l == "a":
            ques_4 = input(
                "\nShe is telling she's not feeling active lately.\n What do you do?\n A. Get active together....\n B. Tell Her that it's Her fault actually\n Choose A or B ")
            ques_4l = ques_4.lower()

            if ques_4l == "a":
                ques_5 = input(
                    "\nShe is telling and you're not understanding anymore.\n What do you do?\n A. Ask your partner what you can do.....\n B. Tell Her you're unable to understand her\n Choose A or B ")
                ques_5l = ques_5.lower()

                if ques_5l == "a":
                    print(
                        "\nWell! At this point whatever she says, take Her to a Romantic Date Night, make some fun stuffs, do some old things what you've done together long ago. It'll make Her realize that whatever happens You'll always be there for Her. End of the Story.")
                else:
                    print("\nLife End!")
            else:
                print("\nLife End!")
        else:
            print("\nLife End!")
    else:
        print("\nLife End!")
else:
    print("\nLife End!")