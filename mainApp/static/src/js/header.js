function addActiveClass(elementClassName, mainAreaID, eventTargetTrue)
{
    const element = document.querySelector(elementClassName);
    const main = document.getElementById(mainAreaID)
    if(eventTargetTrue)
    {
        element.classList.contains('active') ? element.classList.remove('active') : element.classList.add('active');

        if (element.classList.contains('active'))
            main.classList.add('passive')
        else if (!element.classList.contains('active'))
            main.classList.remove('passive')
    }
    else
        element.classList.contains('active') ? element.classList.remove('active') : '';

}

export function toggleMenus(elementIdName, mainAreaID, popUpMenuClassName)
{
    const menuBar = document.getElementById(elementIdName);
    if(menuBar) // person_button is define in html page
    {
        console.log(menuBar)
        let childElement = undefined
        let childElement2 = undefined
        if (menuBar.hasChildNodes())
        {
            if (elementIdName === 'hamburgerMenu')
            {
                childElement = menuBar.querySelector('i');
                if (childElement.hasChildNodes())
                    childElement = childElement.querySelector('img');
            }
            else if (elementIdName === 'avatar')
                childElement2 = menuBar.querySelector('img')
        }
        console.log(childElement);
        document.addEventListener('click', (event)=>{
            if(event.target === menuBar || event.target === childElement || event.target === childElement2)
                addActiveClass(popUpMenuClassName, mainAreaID, true);
            if((event.target != menuBar && event.target != childElement && event.target != childElement2))
                addActiveClass(popUpMenuClassName, mainAreaID, false);
        });
    };
};