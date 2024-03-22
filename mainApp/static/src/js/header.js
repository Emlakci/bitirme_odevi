function addActiveClass(elementClassName, eventTargetTrue)
{
    const element = document.querySelector(elementClassName);
    if(eventTargetTrue)
        element.classList.contains('active') ? element.classList.remove('active') : element.classList.add('active');
    else
        element.classList.contains('active') ? element.classList.remove('active') : '';
}

export function toggleMenus(elementIdName,popUpMenuClassName)
{
    const menuBar = document.getElementById(elementIdName);

    if(menuBar) // person_button is define in html page
    {
        let childElement = undefined
        if (menuBar.hasChildNodes())
        {
            childElement = menuBar.querySelector('i');
        }
        document.addEventListener('click', (event)=>{
            if(event.target === menuBar || event.target === childElement)
                addActiveClass(popUpMenuClassName, true);
            if((event.target != menuBar && event.target != childElement))
                addActiveClass(popUpMenuClassName, false);
        });
    };
};