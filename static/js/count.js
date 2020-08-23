const targetForm = document.querySelector('.jss_content_form')     //document - html//querySelector - 가져올 것
const counted_text = document.querySelector('.counted_text')

targetForm.addEventListener("keyup", function(){
    counted_text.innerHTML = targetForm.vlaue.length
})
                                               