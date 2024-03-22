const product_areas = document.querySelectorAll('#product, #product-trend, #product-list');

export function changeBrowserLocation()
{
    product_areas.forEach((item)=>{
        console.log(item)
        item.addEventListener('click', (event)=>{
            const element = event.target;
            const parent_element = element.parentElement;
            let query = element.className;
            if(query === 'product-img')
            {
                console.log(element, parent_element.getAttribute('data-p-id'))
                const p_id = Number(parent_element.getAttribute('data-p-id'));
                console.log(p_id);
                const currentUrl = window.location.href;
                console.log(currentUrl.toString().includes('productDetails/'))
                if(currentUrl.toString().includes('productDetails/'))
                {
                    const current_id = currentUrl.split('/productDetails/')[1];
                    const newURL = currentUrl.replace(`/productDetails/${current_id}`, `/productDetails/${p_id}`);
                    window.location.href = newURL;
                }
                else
                window.location.href = `productDetails/${p_id}`
            }
        })
    });

}