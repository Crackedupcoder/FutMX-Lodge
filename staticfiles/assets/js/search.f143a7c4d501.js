let body = select('body');
on('click', '.navbar-toggle-box', function(e) {
  e.preventDefault()
  body.classList.add('box-collapse-open')
  body.classList.remove('box-collapse-closed')
})

on('click', '.close-box-collapse', function(e) {
  e.preventDefault()
  body.classList.remove('box-collapse-open')
  body.classList.add('box-collapse-closed')
})
