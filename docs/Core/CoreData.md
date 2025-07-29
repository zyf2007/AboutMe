# 核心档案
## 🌐 如何发现我？

* 🖋️ 网名：胡桃 / hutao_zyf / zyf2007
* 👤 称呼：胡桃酱
* 🖼️ 经常使用的头像：胡桃（原神） / 惠飛須澤胡桃（学园孤岛） / 才羽绿（蔚蓝档案）

## 👩‍💻 固有属性
* 🎂 生日：2007年4月17日
* 🎈 年龄：<span id="years-value">javascript初始化未完成</span>岁
* 💫 星座：♈白羊座
* 🗺️ 出生地：上海徐汇
* 🕗 时区：UTC+08:00
* ⌚ 当前时间：<span id="cur-time">javascript初始化未完成</span>
* 📐 身体质量指数(BMI)：16.1 （更新于2025.6.24）
* 📏 身体围度尺寸：（更新于2025.6.24）
    * 上胸围：73cm ±3cm
    * 腰围：59cm ±3cm
    * 臀围：85cm ±3cm
    * 大腿围：43cm ±2cm
    * 小腿围：34cm ±2cm
    * 腕围：14.5cm ±1cm
## 💕 可变属性（各种问卷）
* MBTI：ESTP
* （想起来了再加）




























<script>
function getFixedChinaTimeString() {
    const date = new Date(Date.now() + (8 * 60 * 60 * 1000));
    const days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    return `${days[date.getUTCDay()]} ${months[date.getUTCMonth()]} ${date.getUTCDate()} ${date.getUTCFullYear()} ${date.getUTCHours().toString().padStart(2, '0')}:${date.getUTCMinutes().toString().padStart(2, '0')}:${date.getUTCSeconds().toString().padStart(2, '0')} GMT+0800 (中国标准时间)`;
}

function initTimeCalculator() {
  const yearsElement = document.getElementById('years-value');
  const timeElement = document.getElementById('cur-time');
  function updateTimeDisplay() {
    const chinaTime = new Date(Date.now() + (8 * 60 * 60 * 1000));
    const age = chinaTime - new Date('2007-04-17T04:00:00Z');
    const years = age / 1000 / 60 / 60 / 24 / 365.2425;
    yearsElement.textContent = years.toFixed(8);
    timeElement.textContent = getFixedChinaTimeString()
  }
  updateTimeDisplay();
  setInterval(updateTimeDisplay, 200);
}
document.addEventListener('DOMContentLoaded', initTimeCalculator);
</script>
