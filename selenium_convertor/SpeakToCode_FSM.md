# Speak to code 
## dictionary
- command : first word in sentence  

## yaml 
All:
  command:
    open: 
      handler:browse()
      synonyms:[browse,]

    




## assumptions
- we save important info in specific yaml which holds known Sites
- for every "known site" we have yaml for every menu item  
- for every menu item we will add a list of other ways of saying  
 
## preWork
- In the start of run the program will build a list of key, value pairs that hav the "sayings"
  as the key , and the base word as the value
 - for every "first word" there would be a function associated 
## Work 
 - User enters text 
 --If *command not in all.command list
    - show *all.command dropdown
    - if other was selected 
        - add command and handler with this name 
        - TODO add description and code
    - elif entry was chosen 
        - add command as synonym to the selected entry
        

    
    
```mermaid
%% Example of sequence diagram
  sequenceDiagram
    Alice->>Bob: Hello Bob, how are you?
    alt is sick
    Bob->>Alice: Not so good :(
    else is well
    Bob->>Alice: Feeling fresh like a daisy
    end
    opt Extra response
    Bob->>Alice: Thanks for asking
    end
```
```mermaid
graph LR
A[Hard edge] -->B(Round edge)
    B --> C{Decision}
    C -->|One| D[Result one]
    C -->|Two| E[Result two]
```

```mermaid
        gantt
        dateFormat  YYYY-MM-DD
        title Adding GANTT diagram functionality to mermaid

        section A section
        Completed task            :done,    des1, 2014-01-06,2014-01-08
        Active task               :active,  des2, 2014-01-09, 3d
        Future task               :         des3, after des2, 5d
        Future task2               :         des4, after des3, 5d

        section Critical tasks
        Completed task in the critical line :crit, done, 2014-01-06,24h
        Implement parser and jison          :crit, done, after des1, 2d
        Create tests for parser             :crit, active, 3d
        Future task in critical line        :crit, 5d
        Create tests for renderer           :2d
        Add to mermaid                      :1d

        section Documentation
        Describe gantt syntax               :active, a1, after des1, 3d
        Add gantt diagram to demo page      :after a1  , 20h
        Add another diagram to demo page    :doc1, after a1  , 48h

        section Last section
        Describe gantt syntax               :after doc1, 3d
        Add gantt diagram to demo page      : 20h
        Add another diagram to demo page    : 48h
```