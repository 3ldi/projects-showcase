window.addEventListener('DOMContentLoaded', (event) => {
    console.log('DOM fully loaded and parsed');

    // Hide the get in touch form container and alert message by default
    const contactFormDiv = document.querySelector('#contact-form-div');
    contactFormDiv.style.display = 'none';

    // Select the get in touch button
    const contactBtn = document.querySelector('#get-in-touch');

    // Select the Cancel button
    const cancelBtn = document.querySelector('#cancel-msg');


    // Add an onclick event listener to display the form
    contactBtn.addEventListener('click', () => {
        if (contactFormDiv.style.display == 'none') {
            // Display the form and hide the get in touch button
            contactFormDiv.style.display = 'block';
            contactBtn.style.display = 'none';
        }
    });

    // Call function wordCount to hint the user about the message length
    wordCount();

    // Add event listener to hide the form and display the get in touch button
    cancelBtn.addEventListener('click', () => {
        contactFormDiv.style.display = 'none';
        contactBtn.style.display = 'block';
    });
}); // end DomContentLoaded function


function wordCount() {
    // Create variable myText to access text area in the page
    const myText = document.getElementById("id_message_body");

    // Get the text Area hint element and hide it by default
    const wordCountHint = document.getElementById("word-count-hint");
    wordCountHint.style.display = "none";

    // Add event handler to variable myText
    myText.onkeyup = function () {
        let totalWords = 0;
        let textEntered = document.getElementById("id_message_body").value;

        if (textEntered.length > 0) {
            // Create an array with all the words in the string. 
            // Words are split at every new-line character "\n".
            const textArray = textEntered.trim().split("\n");

            // Create string newText wich contains no new-line characters.
            // Words are separated with one white space.
            let newText = "";
            for (let i = 0; i < textArray.length; i++) {
                newText += textArray[i];
                newText += " ";
            }

            // Create the final array containing all the words by spliting the newText string
            // at every white space.
            const finalTextArr = newText.trim().split(" ");

            /*
            * Loop each element of the array and count as words only those 
            * elements that are different form white spaces.
            */
            for (let i = 0; i < finalTextArr.length; i++) {
                if (finalTextArr[i] != "") {
                    totalWords += 1;
                }  // end if
            } // end for       
        } // end main if

        // Acces span element with id="words-left" and change its value to totalWords
        document.getElementById("words-left").innerHTML = totalWords;

        // Display a hint to user if more than 150 words were used
        if (totalWords > 150) {
            // display the word count hint
            wordCountHint.style.display = 'block';
        } else {
            // hide the word count hint
            wordCountHint.style.display = 'none';
        }
    }
}// end function

