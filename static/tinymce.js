const script = document.createElement('script')

script.src ='https://cdn.tiny.cloud/1/x46v6pt7hefbcf52ukfx4ixr0dyieid5bjz2dlbv2ws3rt4b/tinymce/7/tinymce.min.js'
script.defer = true
document.head.appendChild(script)

script.onload = function(){

    tinymce.init({
        selector: '#id_content',
        width: 600,
        height: 300,
        plugins: [
          'advlist', 'autolink', 'link', 'image', 'lists', 'charmap', 'preview', 'anchor', 'pagebreak',
          'searchreplace', 'wordcount', 'visualblocks', 'visualchars', 'code', 'fullscreen', 'insertdatetime',
          'media', 'table', 'emoticons', 'help'
        ],
        toolbar: 'undo redo | styles | bold italic | alignleft aligncenter alignright alignjustify | ' +
          'bullist numlist outdent indent | link image | print preview media fullscreen | ' +
          'forecolor backcolor emoticons | help',
        menu: {
          favs: { title: 'My Favorites', items: 'code visualaid | searchreplace | emoticons' }
        },
        menubar: 'favs file edit view insert format tools table help',
        content_css: 'css/content.css'  });
    
}