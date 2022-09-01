;(function () {
  'use strict'

  function findFirstMenu(target, root) {
    if (target == undefined) return
    if (target == root) return
    if (
      target.tagName === 'BUTTON' &&
      target.classList.contains('btn_opentype')
    ) {
      return target
    }
    return findFirstMenu(target.parentElement, root)
  }

  function findThirdMenu(target, root) {
    if (target == undefined) return
    if (target == root) return
    if (target.tagName === 'A' && target.classList.contains('link_detailidx')) {
      return target
    }
    return findThirdMenu(target.parentElement, root)
  }

  function findMenuRoot(target, root) {
    if (target == undefined) return
    if (target == root) return
    if (target.classList.contains('list_opentype')) return target
    return findMenuRoot(target.parentElement, root)
  }

  function selectThirdMenu(selectedMenu, root) {
    const menus = root.querySelectorAll('a.link_detailidx')
    const subMenus = root.querySelectorAll('a.sub_link_detailidx')
    menus.forEach(function (menu) {
      menu.classList.remove('on')
    })
    subMenus.forEach(function (subMenu) {
      subMenu.classList.remove('on')
    })
    selectedMenu && selectedMenu.classList.add('on')
  }

  function selectFourthMenu(selectedMenu, root) {
    const menus = root.querySelectorAll('a.sub_link_detailidx')
    menus.forEach(function (menu) {
      menu.classList.remove('on')
    })
    selectedMenu && selectedMenu.classList.add('on')
  }

  window.addEventListener('DOMContentLoaded', function () {
    const docsRoot = document.querySelector('#docsRoot')
    const menuRoot = document.querySelector('#mFeature.menu_side')
    const menuArea = menuRoot.querySelector('.area_sidemenu')
    const floatingArea = document.querySelector('.floating_menu')

    function initMenu() {
      menuArea.addEventListener('click', function (e) {
        const menu1 = findFirstMenu(e.target, menuArea)
        if (menu1) {
          e.preventDefault()
          e.stopPropagation()

          const root = findMenuRoot(menu1, menuArea)
          root.classList.toggle('open_on')
        }

        const menu3 = findThirdMenu(e.target, menuArea)
        if (menu3) {
          docsRoot.classList.remove('menu_on')
          menuRoot.classList.remove('menuside_on')
          selectThirdMenu(menu3, menuArea)
        }
      })
    }

    function initLNBScroll() {
      const selectedLNBSubMenu = document.querySelector(
        '.list_defaulttype > .on'
      )
      const selectedLNBMenu =
        selectedLNBSubMenu?.parentElement?.parentElement?.parentElement
      if (selectedLNBMenu) {
        const LNBArea = document.querySelector('.menu_side')
        LNBArea.scrollTo(0, selectedLNBMenu.offsetTop)
      }
    }

    function initScrollMenuSelector() {
      const getScrollHeight = (e) => {
        const body = document.body
        const html = document.documentElement

        return Math.max(
          body.scrollHeight,
          body.offsetHeight,
          html.clientHeight,
          html.scrollHeight,
          html.offsetHeight,
          e.target.scrollHeight || 0
        )
      }

      const getClientHeight = () => {
        const html = document.documentElement
        return html.clientHeight || window.innerHeight
      }

      function selectMenuFromTitle(title, root) {
        const selectedMenu = root.querySelector(
          `a.link_detailidx[href='#${title.id}']`
        )
        return selectedMenu
      }

      function selectSubMenuFromTitle(title, root) {
        const selectedMenu = root.querySelector(
          `a.sub_link_detailidx[href="#${title.id}"]`
        )
        return selectedMenu
      }

      function selectSubTitles(subTitles, currentTitle, nextTitle) {
        const result = []
        subTitles.forEach(function (title) {
          if (
            title.offsetTop > currentTitle.offsetTop &&
            title.offsetTop < (nextTitle.offsetTop || Number.MAX_SAFE_INTEGER)
          )
            result.push(title)
        })
        return result
      }

      function checkMaxHeightChanged(floatingArea, baseMaxHeight) {
        return floatingArea.style.maxHeight !== baseMaxHeight + 'px'
      }

      window.addEventListener(
        'scroll',
        function (e) {
          const targetClassList = Array.from(e.target.classList || [])
          if (
            targetClassList.includes('floating_menu') ||
            targetClassList.includes('menu_side')
          ) {
            return
          }

          var scrollPosition = window.scrollY || e.target.scrollTop || 0
          var offsetHeight = getClientHeight()
          var scrollHeight = getScrollHeight(e)
          var titleList = document.querySelectorAll(
            '#mArticle h3 .heading-offset-anchor'
          )
          var subTitleList = document.querySelectorAll(
            '#mArticle h4 .heading-offset-anchor'
          )
          titleList.forEach(function (title, index) {
            if (scrollPosition < title.offsetTop + 128) return
            const selectedMenu = selectMenuFromTitle(title, menuArea)
            selectThirdMenu(selectedMenu, menuArea)
            if (floatingArea) {
              const selectedFloatingMenu = selectMenuFromTitle(
                title,
                floatingArea
              )
              selectThirdMenu(selectedFloatingMenu, floatingArea)

              const nextTitle = titleList[index + 1] || {}
              const subTitles = selectSubTitles(subTitleList, title, nextTitle)
              subTitles.forEach(function (subTitle, index) {
                if (index === 0 || scrollPosition >= subTitle.offsetTop + 152) {
                  const selectedFloatingMenu = selectSubMenuFromTitle(
                    subTitle,
                    floatingArea
                  )
                  return selectFourthMenu(selectedFloatingMenu, floatingArea)
                }
              })
            }
          })

          // end
          if (Math.ceil(offsetHeight + scrollPosition) >= scrollHeight) {
            const lastTitle = titleList[titleList.length - 1]
            const selectedMenu = selectMenuFromTitle(lastTitle, menuArea)
            selectThirdMenu(selectedMenu, menuArea)

            if (floatingArea) {
              const selectedFloatingMenu = selectMenuFromTitle(
                lastTitle,
                floatingArea
              )
              selectThirdMenu(selectedFloatingMenu, floatingArea)
              const lastSubTitles = selectSubTitles(subTitleList, lastTitle, {})
              if (lastSubTitles.length) {
                const selectedSubFloatingMenu = selectSubMenuFromTitle(
                  lastSubTitles[lastSubTitles.length - 1],
                  floatingArea
                )
                selectFourthMenu(selectedSubFloatingMenu, floatingArea)
              }
            }
          }

          // 스크롤 위치에 따른 플로팅메뉴 height 조절
          if (floatingArea) {
            const footerHeight = 70
            const baseMaxHeight = offsetHeight - 210
            if (scrollHeight < offsetHeight + scrollPosition + footerHeight) {
              const offset =
                offsetHeight + scrollPosition + footerHeight - scrollHeight
              floatingArea.style.maxHeight = baseMaxHeight - offset + 'px'
            } else if (checkMaxHeightChanged(floatingArea, baseMaxHeight)) {
              floatingArea.style.maxHeight = baseMaxHeight + 'px'
            }
          }
        },
        true
      )
    }

    function initResponsivePCMenuBtn() {
      const menuOpenBtn = document.querySelector('button.btn_menuopen')
      const menuCloseBtn = document.querySelector('button.btn_menuclose')

      menuOpenBtn.addEventListener('click', function (e) {
        e.stopPropagation()
        e.preventDefault()
        docsRoot.classList.add('menu_on')
      })
      menuCloseBtn.addEventListener('click', function (e) {
        e.stopPropagation()
        e.preventDefault()
        docsRoot.classList.remove('menu_on')
      })
    }

    function initMobileMenuBtn() {
      const menuToggleBtn = menuRoot.querySelector('button.btn_menutoggle')

      menuToggleBtn.addEventListener('click', function (e) {
        e.stopPropagation()
        e.preventDefault()
        menuRoot.classList.toggle('menuside_on')
        handleMobileMenuClick()
      })

      initMobileMenuScrollTop()
    }

    function handleMobileMenuClick() {
      // const opened = menuRoot.classList.contains('menuside_on')
      initMobileMenuScrollTop(menuRoot)
    }

    function initMobileMenuScrollTop() {
      const innerMenu = menuRoot.querySelector('.inner_side')
      const selected = menuRoot.querySelector('.list_defaulttype > li.on')
      const selectedBranch = closestElement(selected, 'list_opentype')
      if (!innerMenu || !selected || !selectedBranch) return

      innerMenu.scrollTop = selected.offsetTop + selectedBranch.offsetTop
    }

    function closestElement(el, className) {
      if (!el) return null
      if (el.closest) return el.closest('.' + className)

      if (el.classList.contains(className)) return el
      else return closestElement(el.parentElement, className)
    }

    initMenu()
    initLNBScroll()
    initScrollMenuSelector()
    initResponsivePCMenuBtn()
    initMobileMenuBtn()
  })
})()
