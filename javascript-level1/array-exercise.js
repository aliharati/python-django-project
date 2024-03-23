run()

function run(){
    var start = prompt("would you like to start the web app?y/n ")
    if(start=="y"){
        studentApp()
    }else{
        quit()
    }
}
function studentApp(){
    var quit = false;
    var students = []
    while(!quit){
        var input = prompt("Please select an action: add, remove, display, or quit.")
        switch(input){
            case "add":
                students.push(prompt("What name would you like to add? "))
                console.log("student added")
                break;
            case "remove":
                var rm = prompt("What name would you like to remove?")
                for(var i=0; i<students.length;i++){
                    if(students[i]===rm){
                        students.splice(i,1);
                    }
                }
                break;
            case "display":
                console.log(students);
                break;
            case "quit":
                quit = true
                quit()
                break;
            default:
                break;
                
        }
    }
}
function quit(){
    alert("Thanks for using the Web App! Please refresh the page to start over.")
}