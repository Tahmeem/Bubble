

let root = document.documentElement;
const section1 = document.querySelector('.header')

window.addEventListener('scroll', () => {
  const y = 1 + (window.scrollY || window.pageYOffset);
   root.style.setProperty('--gradient-percent', y * 4 + "px");
  console.log(y)
})

