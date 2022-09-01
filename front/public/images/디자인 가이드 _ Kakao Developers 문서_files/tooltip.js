;(function () {
  'use strict'
  window.addEventListener('DOMContentLoaded', function () {
    const tooltips = document.querySelectorAll('.tooltip')

    function moveTooltip(tooltipBox, distance) {
      tooltipBox.style.setProperty('left', 'calc(50% + ' + distance + 'px)')
      tooltipBox.style.setProperty('--arrow-margin-left', -5 - distance + 'px')
    }

    function resetTooltipPosition(tooltipBox) {
      tooltipBox.style.setProperty('left', null)
      tooltipBox.style.setProperty('--arrow-margin-left', null)
    }

    function initTooltip() {
      tooltips.forEach((tooltip) => {
        tooltip.addEventListener('mouseover', function () {
          const tooltipBox = this.lastChild
          if (!tooltipBox) return

          const { x, width } = tooltipBox.getBoundingClientRect()
          const maxOffsetX = window.innerWidth - 16

          if (x < 16) {
            moveTooltip(tooltipBox, Math.abs(x - 16))
          } else if (x + width > maxOffsetX) {
            moveTooltip(tooltipBox, -1 * Math.abs(x + width - maxOffsetX))
          }
        })
      })

      tooltips.forEach((tooltip) => {
        tooltip.addEventListener('mouseout', function () {
          const tooltipBox = this.lastChild
          if (!tooltipBox) return

          setTimeout(function () {
            resetTooltipPosition(tooltipBox)
          }, 200)
        })
      })
    }

    initTooltip()
  })
})()
