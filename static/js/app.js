// define a javascript class
class Chatbox{
    // define the constructor
    constructor(){
        // define  the vars that we will be using in the argument
        this.args = {
            open_button: document.querySelector(".chatbox-button"),
            chatbox: document.querySelector(".chatbox-support"),
            send_button: document.querySelector(".send-button"),
            typing: document.querySelector(".typing-bubble")
        }
        this.state = false; // initial state of chatbox - chatbox is initially closed by default
        this.messages = [{name: "welcome-msg", message: "Hi! I am Sydney Bot, thanks for taking a look at my creator's profolio!"},{name: "welcome-msg", message: "How can I help you today?"}]; // array to store messages
        this.loading = false;
    }

    // function to display the messages
    display()
    {
        // Extract the arguments
        const{open_button, chatbox, send_button} = this.args;
        this.updateChatbox(chatbox)
        console.log("testing");
        // add two click event listeners
        // open chatbox when clicked
        open_button.addEventListener("click", () => this.toggleState(chatbox));
        // send msg when click on send button
        send_button.addEventListener("click", () => this.onSendButton(chatbox));
        
        const node = chatbox.querySelector("textarea");
        // Also sends a msg if users use "ENTER" key
        node.addEventListener("keyup", ({key, shiftKey}) =>
        {
            if(key === "Enter" && !shiftKey)
            {
                this.onSendButton(chatbox);
            }
        }) 
    }

    // implement the toggleState function to check if checkbox is open or closed
    toggleState(chatbox)
    {
        this.state = !this.state;
        console.log("worked");
        // show or hides the box
        if(this.state)
        {
            // if initially off, then open chatbox
            chatbox.classList.add("chatbox--active");
        }
        else
        {
            // otherwise close chatbox
            chatbox.classList.remove("chatbox--active");
        }
    }

    load(loading)
    {
        if(this.loading === true)
        {
            typing.style.display = 'block';
        }
        else
        {
            typing.style.display = 'none';
        }
    }
    // implement the send message on send function
    onSendButton(chatbox)
    {
        this.loading = true;
        this.load(this.loading);
        var text_field = chatbox.querySelector("textarea");
        let text1 = text_field.value;
        text_field.style.height = "30px";
        // check if input is an empty message, if it is then just return nothing
        if(text1 === "")
        {
            return;
        }
        // otherwise if text is not empty, then continue
        let msg1 = {name: "User", message: text1}; // define a javascript object (like a dictionary) for the msg that we want to send to our model. The "message" key has to be the same as the key define in out app.py file (line 16)
        this.messages.push(msg1); // push the msg into the message array

        // we want to send a POST request to the predict route at the script root
        fetch($SCRIPT_ROOT + "/predict",
        {
            method: "POST", // define as a POST method
            body: JSON.stringify({message: text1}), // stringify the message to a JSON object
            mode: "cors", // allow Cros Origin Resource Sharing - need this if we are deploying FLASK completely separately from the html
            headers:
            {
                "Content-Type": "application/json" // specify json
            }
        })
        // wait to receive the json response after sending POST request
        .then(r => r.json()) // extract the json obj
        // send the msg back to the user (display it in chatbox)
	.then(r => {
            // create a json obj to store the received msg
            let msg2 = {name: "Sydney Bot", message: r.answer}; // the key has to be the same (answer)
            this.messages.push(msg2); // add the msg to the msg array
            setTimeout(() => this.updateChatbox(chatbox), 600);
            text_field.value = ""; // return/show nothing
        })
	//.then(function (bodyText) {
        //	console.log('Received the following instead of valid JSON:', bodyText);
    	//})
	.catch((error) => {
	    console.log('Error parsing JSON from response')
            console.error("Error:", error);
            this.updateChatbox(chatbox);
            text_field.value = ""; // return/show nothing
        });
    }

    //implement the update chatbox function
    updateChatbox(chatbox)
    {
        
        this.loading = false;
        this.load(this.loading);
        var html = "";
        // loop thru the msgs
        this.messages.slice().reverse().forEach(function(item, index){
            // check if the msg is from user or from our bot (Sydney bot)
            if(item.name === "welcome-msg")
            {
                // modify the innerhtml codes
                html += "<div class = 'messages-item messages-item--operator welcome-msg'>" + item.message + "</div>";
            }
            else if(item.name === "Sydney Bot")
            {
                // modify the innerhtml codes
                html += "<div class = 'messages-item messages-item--operator'>" + item.message + "</div>";
            }
            else
            {
                // modify the innerhtml codes
                html += "<div class = 'messages-item messages-item--visitor'>" + item.message + "</div>";
            }
        });
        // create new html text
        const chat_message = chatbox.querySelector(".chatbox-messages");
        chat_message.innerHTML = html;
    }
}

// Call the class to use it
const chatbox = new Chatbox(); // create an obj called chatbox
chatbox.display();