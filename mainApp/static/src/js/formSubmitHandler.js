import { Message } from "./messageBox.js";

formFetchDataHandler();


//~ function that posts requests ~//
async function submitForm (formId)
{
    let form = document.getElementById(formId);
    const formData = new FormData(form);
    console.log(csrfToken)
    formData.append('csrfmiddlewaretoken',csrfToken);

    try 
    {
        // send form to backend
        const response = await fetch (`/${formId}`, {
            method: 'POST',
            headers: {
                'X-CSRFToken' : csrfToken
            },
            body: formData
        });    
        // control response
        let responseData = await response.json();
        let msgType = String('');
        console.log(response, response.status, responseData);
         
        // parameter did not matched!
        if (response.status == 401) msgType = 'error';
        // Input areas are null
        else if (response.status == 400) msgType = 'error';
        // authentication is successful
        else if (response.status == 200 || response.status == 202) msgType = 'success';
        // registeration is unsuccessful
        else if (response.status == 203) msgType = 'error';

        // create message
        const messageBox = new Message(responseData.message, msgType);
        if (msgType === 'success') 
        {
            const currentURL = window.location.href;
            const direction = formId === 'login' ? '/' : '/login';
            const newURL = currentURL.replace(`/${formId}`, direction);
            location.href = newURL;
        } 
    } 
    catch (error)
    {
        console.log(error);    
    };
};



function formFetchDataHandler()
{
    const form = document.querySelector('form');
    form.addEventListener('submit', (event)=>{
        event.preventDefault();
        submitForm(form.id);
    });
}