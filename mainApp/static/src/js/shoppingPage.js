//+ Constants +//
const productBigImg = document.getElementById('p-main-img');
const productSmallImg = document.querySelectorAll('.p-img.small');
//+ Constants +//

export function changeMainImg ()
{
    productSmallImg.forEach((item)=>{
        item.addEventListener('click', (event)=>{
            productBigImg.src = event.target.src;
        })
    });    
};


