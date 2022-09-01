window.addEventListener('DOMContentLoaded', (event) => {
  var tabHeaders = document.querySelectorAll('.tabs .tab-header')
  var tabBody = document.querySelectorAll('.tabs .tab-body')
  tabHeaders.forEach(function (tabHeader) {
    tabHeader.children[0].classList.add('tab_selected')
    var tabs = Array.from(tabHeader.children)
    tabs.forEach(function (tab) {
      tab.onclick = function (e) {
        var filteredTabs = includeTab(this.classList[0], tabHeaders)
        toggleTab(this.classList[0], filteredTabs, 'tab_selected')
        var filteredTabBody = includeTab(this.classList[0], tabBody)
        toggleTab(this.classList[0], filteredTabBody, 'tab_body_selected')
      }
    })
  })

  tabBody.forEach(function (tabBodyItem) {
    tabBodyItem.children[0].classList.add('tab_body_selected')
  })

  function includeTab(tabId, tabItems) {
    var filteredTabItems = Array.from(tabItems).filter(function (tabItem) {
      var filteredTabItem = Array.from(tabItem.children).filter(function (tab) {
        return tab.classList.contains(tabId)
      })
      return filteredTabItem.length > 0
    })
    return filteredTabItems
  }

  function toggleTab(tabId, tabItems, className) {
    tabItems.forEach(function (tabItem) {
      var tabs = Array.from(tabItem.children)
      tabs.forEach(function (tab) {
        if (tab.classList.contains(tabId)) {
          tab.classList.add(className)
        } else {
          tab.classList.remove(className)
        }
      })
    })
  }
})
