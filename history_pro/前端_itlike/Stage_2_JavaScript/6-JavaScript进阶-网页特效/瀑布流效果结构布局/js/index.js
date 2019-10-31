/**
 * Created by xiaoming
 * 创建日期: 2019/3/30
 * 创建时间: 18:36
 */

window.onload = function () {
    // 实现瀑布流布局
    // waterFull("main","box");
    waterFull("main", "box");
};

/**
 * 瀑布流布局
 */
function waterFull(parent, child) {
    // 1.父盒子居中
    // 给父盒子设置一个宽度
    // 1.1获取所有的子盒子
    var allBox_temp = $(parent);
    // console.log(allBox_temp);
    var allBox = allBox_temp.getElementsByClassName(child);
    // console.log(allBox);
    // 1.2获取子盒子的宽度
    var boxWidth = allBox[0].offsetWidth;
    // console.log(boxWidth);

    // 获取盒子的列数
    // 1.3 获取屏幕的宽度
    var screenW = document.documentElement.clientWidth;
    // console.log(screenW);
    // 1.4求出列数
    // 屏幕宽度 除以 列数
    // var cols = screenW / boxWidth;
    // 取整数
    var cols = parseInt(screenW / boxWidth);
    // console.log(cols);
    // 1.5父盒子居中
    $(parent).style.width = cols * boxWidth + 'px';
    $(parent).style.margin = "0 auto";

    // 2子盒子的定位
    // 2.1 定义高度数组
    var heightArr = [];
    var boxHeight = 0;
    var minBoxHeight = 0;
    var minBoxIndex = 0;



    // 2.2 遍历子盒子
    for(var i=0; i < allBox.length; i++){
        // 2.2.1求出每一个子盒子的高度
        boxHeight = allBox[i].offsetHeight;
        // console.log(boxHeight);
        // 2.2.2 取出第一行盒子的高度,放入第一行高度数组
        // 判断是不是第一行,i要是小于总列数就是在第一行了
        if(i < cols){
            heightArr.push(boxHeight);
        }
        else{
            // // 剩余行
            // // 1.取出最矮的盒子高度
            // // 方法1
            // // minBoxHeight = Math.min.apply(this, heightArr);
            // // 方法2
            // // 没有这个方法,需要借调一个方法
            minBoxHeight = _.min(heightArr);
            // // 2.求出最矮盒子对应的索引
            // // 需要各个来写一个盒子来求
            minBoxIndex = getMinBoxIndex(heightArr, minBoxHeight);
            // // 3子盒子定位
            allBox[i].style.position = 'absolute';
            /**
             * 这个position可真的让我找的好酒
             * md
             * 有瑕疵,这编辑器
             * positon他不报错
             * 我找不到错误就
             * ........
             * 服了 奥
             *
             */



            // // console.log("来来来");
            allBox[i].style.left = minBoxIndex * boxWidth + 'px';
            allBox[i].style.top = minBoxHeight + 'px';
            // // 4. 更新数组中的高度
            heightArr[minBoxIndex] += boxHeight;


        }

    }
    // console.log(minBoxIndex);



}

function $(id) {
    return typeof id === "string" ? document.getElementById(id) : null;
}

function getMinBoxIndex(arr, value) {
    for(var i=0; i < arr.length; i++){
        if(arr[i] === value){
            return i;
        }
    }

}

