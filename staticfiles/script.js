document.addEventListener("DOMContentLoaded", () => {
    // aos
    AOS.init();


    // typed js
    // var typed3 = new Typed('#title-for-typed', {
    //     strings: [' <span>Innovatsiyalar</span> va <span>innovatorlarni</span> ishlab chiqaruvchi maydon ', ' <span>Hazil</span> aslida esa  <span>IT kasblarni</span> o\'rgatadigan markaz', 'Umuman olganda, ikkisi ham <span>amalga</span> oshiriladi'],
    //     typeSpeed: 20,
    //     backSpeed: 14,
    //     smartBackspace: true, // this is a default
    //     loop: true
    // });




    let all = document.querySelectorAll("body > *:not(script)")
    const opener = document.querySelector(".opener")
    const closer = document.querySelector(".times")
    const resNav = document.querySelector("#navbar .navbar-content ul")
    const lists = document.querySelectorAll("#navbar .navbar-content ul a")

    // responsive navbar
    opener.addEventListener("click", () => {
        if (!resNav.classList.contains("tr-0")) {
            resNav.classList.add("tr-0");
        }
    })
    closer.addEventListener("click", () => {
        if (resNav.classList.contains("tr-0")) {
            resNav.classList.remove("tr-0");
        }
    })
    lists.forEach(list => {
        list.addEventListener("click", () => {
            if (resNav.classList.contains("tr-0")) {
                resNav.classList.remove("tr-0");
            }
        })
    })


    // all.forEach(all => {
    //     if (all.classList.contains("light")) {
    //         all.classList.remove("light")
    //         all.classList.add("dark")
    //         console.log(all)
    //     }
    //     else {
    //         all.classList.add("light")
    //         all.classList.remove("dark")

    //     }
    // })




    let accardion = document.querySelector("#accardion")
    let accardionsspan = document.querySelector("#accardion span")


    let root = document.querySelector(":root")
    let mode = document.querySelector(".mode i")


    // LocalStorage'da 'status' mavjudligini tekshirish va boshlang'ich qiymat o'rnatish
    if (localStorage.getItem("status") === null) {
        localStorage.setItem("status", "true"); // Boshlang'ich qiymatni o'rnatish faqat bir marta
    }

    // Temani localStorage'dagi 'status' qiymatiga qarab qo'llash
    function applyTheme() {
        const status = localStorage.getItem("status");

        if (status === "true") {
            // Light Mode (true holati)
            mode.classList.remove("lni-sun");
            mode.classList.add("lni-night");
            root.style.setProperty("--color-body", "#fff");
            root.style.setProperty("--color-text", "#0F1214");
            root.style.setProperty("--color-text-04", "#0F121440");
            root.style.setProperty("--color-body-2", "#E8EAEE");
            if (accardion) {
                accardion.style.backgroundColor = "#fff";
                accardionsspan.style.color = "var(--color-span)";
            }
            // if(document.querySelector("#main-2")){
            //     let main2 = document.querySelector("#main-2")
            //     main2.style.backgroundColor = "#007FFF"
            // }
        } else {
            // Dark Mode (false holati)
            mode.classList.remove("lni-night");
            mode.classList.add("lni-sun");
            root.style.setProperty("--color-body", "#0F1214");
            root.style.setProperty("--color-text", "#fff");
            root.style.setProperty("--color-text-04", "#ffffff40");
            root.style.setProperty("--color-body-2", "#0F1214");
            if (accardion) {
                accardion.style.backgroundColor = "var(--color-span)";
                accardionsspan.style.color = "#000";
            }

            if(document.querySelector(".main-courses")){
                let main2 = document.querySelector(".main-courses")
                main2.style.cssText = "background-color: #007FFF !important;"
                const span = document.querySelector('#main-2 .left-side h2 span');
                span.style.color = "var(--color-body)"
            }
        }
    }

    // Temani almashtirish
    function toggleTheme() {
        const status = localStorage.getItem("status");
        // Statusni o'zgartirish va localStorage'ga saqlash
        localStorage.setItem("status", status === "true" ? "false" : "true");

        // Yangilangan holatni qo'llash
        applyTheme();
    }

    // Dastlabki tema holatini qo'llash
    applyTheme();

    // Event listener qo'shish
    mode.addEventListener("click", toggleTheme);














    // swiper 1
    let swiper = new Swiper(".mySwiper", {
        effect: "coverflow",
        grabCursor: true,
        centeredSlides: false,
        loop: true,
        slidesPerView: 1.1,
        spaceBetween: 30,
        autoplay: {
            delay: 4000,
            disableOnInteraction: false,
        },

        coverflowEffect: {
            rotate: 30,
            stretch: 30,
            depth: 300,
            modifier: 1,
            slideShadows: true,
        },

        breakpoints: {
            480: {
                slidesPerView: 1.3,
                spaceBetween: 20,
            },
            640: {
                slidesPerView: 1.5,
                spaceBetween: 20,
            },
            768: {
                slidesPerView: 2,
                spaceBetween: 40,
                centeredSlides: true,
            },
            1200: {
                slidesPerView: 3.1,
                spaceBetween: 40,
            },

        },
    });




    let swiperTeam = new Swiper(".swiperTeam", {
        slidesPerView: 1.4,
        spaceBetween: 20,
        loop: true,
        breakpoints: {
            480: {
                slidesPerView: 1.5,
            },
            576: {
                slidesPerView: 1.5,
            },
            768: {
                slidesPerView: 2.1,
            },
            992: {
                slidesPerView: 3.1
            },
            1200: {
                slidesPerView: 3.5
            },
            1400: {
                slidesPerView: 4.1
            }
        },


    });




    // foto lavhalar

    const swiperPhoto = new Swiper(".swiper-container", {
        freeMode: true, // Enables free mode for continuous movement
        loop: true, // Loops the slides indefinitely
        autoplay: {
            delay: 0, // No delay between slides, continuous scrolling
            disableOnInteraction: false, // Keeps autoplay going after interaction
            reverseDirection: false, // Direction of scrolling (optional)
        },
        speed: 3000, // Sets the scroll speed (in ms)
        slidesPerView: 4.5, // Automatically adjusts the number of slides visible
        spaceBetween: 10, // Adjusts space between slides
        transitionTimingFunction: "linear", // Ensures constant speed without easing
        centeredSlides: false, // Disables centering the current slide (optional)
    });



    //   autoslider
    const scrollingDiv = document.getElementById('scrollingDiv');
    const scrollingDiv2 = document.getElementById('scrollingDiv2');

    function startScroll() {
        scrollingDiv.style.animationPlayState = 'running';
    }

    function pauseScroll() {
        scrollingDiv.style.animationPlayState = 'paused';
    }

    // Yaratilgan slayderning davomiyligini uzaytirish uchun elementlarni dubl qilish
    for (let i = 0; i < 5; i++) { // 3 marta ko‘paytirish uchun
        if (scrollingDiv && scrollingDiv2) {
            scrollingDiv.innerHTML += scrollingDiv.innerHTML;
            scrollingDiv2.innerHTML += scrollingDiv2.innerHTML;
        }
    }

})