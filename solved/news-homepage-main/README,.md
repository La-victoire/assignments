# Frontend Mentor - News homepage solution

This is a solution to the [News homepage challenge on Frontend Mentor](https://www.frontendmentor.io/challenges/news-homepage-H6SWTa1MFl). Frontend Mentor challenges help you improve your coding skills by building realistic projects. 

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Screenshot](#screenshot)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#HTML,CSS)
  - [What I learned](#what-i-learned)
  - [Continued development](#continued-development)
  - [Useful resources](#Youtube,chatgpt)
- [Author](#La_victoire.dev)
- [Acknowledgments](#acknowledgments)


## Overview

### The challenge

Users should be able to:

- View the optimal layout for the interface depending on their device's screen size
- See hover and focus states for all interactive elements on the page

### Screenshot

![design/desktop-design.jpg]



### Links

- Solution URL: [https://assignments-cjz7l9zx9-victory-s-projects-b4adadd8.vercel.app/](https://assignments-cjz7l9zx9-victory-s-projects-b4adadd8.vercel.app/)
- Live Site URL: [https://assignments-cjz7l9zx9-victory-s-projects-b4adadd8.vercel.app/]()

## My process

### Built with

- Semantic HTML5 markup
- CSS custom properties
- Flexbox
- CSS Grid
- Mobile-first workflow



### What I learned

I learn't quite a bit from this project like how to edit evets without javascript
i'm greatful for the opportunuty to learn 

```html
 <nav class="nav">
    <label for="nav-btn" class="close-btn">
      <img class="close-btn" src="assets/images/icon-menu-close.svg" alt="">
    </label>
    <div class="tabs">

      <div class="hm"> 
        Home 
      </div>
      <div class="nw">
        New
      </div>
      <div class="pplr">
        Popular
      </div>
      <div class="trnd">
        Trending
      </div>
      <div class="ctgr">
        Categories
  
    </div>

  </nav>
```
```css
.nav{
    position: fixed;
    top: 0;
    right: -300px;
    width: 250px;
    height: 100%;
    background-color: hsl(36, 100%, 99%) ;
    color: black;
    padding: 20px;
    transition: right 0.3s ease;
  }
  .tog:checked~ .nav , .ham{
    right: 0;
  }
```



### Continued development

Flexbox has been pretty tricky for me but i intend to get better no matter what as well as in javascript


### Useful resources

- [https://www.youtube.com/watch?v=PL3Odw-k8W4&t=70s] - I got my inspiration for the mobile responsiveness from this video and i suggets others go for it.



## Author

- Website - [https://www.la-victoire.github.io/portfolio_test/?tab=home]
- Frontend Mentor - [https://www.frontendmentor.io/profile/La-victoire]
- Twitter - [https://www.frontendmentor.io/profile/La-victoire]


## Acknowledgments

I'd like to thank the community for the support and the resources they provide. I'm grateful for their advice and also i just want to give a shout out to chatgpt and youtube. lol :)


