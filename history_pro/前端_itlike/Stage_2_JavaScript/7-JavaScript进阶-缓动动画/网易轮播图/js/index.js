/**
 * Created by xiaoming
 * 创建日期: 2019/4/4
 * 创建时间: 22:25
 */

window.onload = function () {
    // alert("miemaobing");
    // 获取标签
    var slider = $("slider");
    var slider_main = $("slider_main");
    var slider_main_img = slider_main.children;
    var slider_ctl = slider.children[1];

    // 2动态创建爱你指示器
    for(var i=0;i<slider_main_img.length;i++){
        var span = document.createElement("span");
        span.className = "slider-ctl-icon";
        slider_ctl.insertBefore(span, slider_ctl.children[1]);

    }

    // 让第一个选中3
    slider_ctl.children[1].className = "slider-ctl-icon current";
};




/*

                            _ooOoo_
                           o8888888o
                           88" . "88
                           (| -_- |)
                            O\ = /O
                        ____/`---'\____
                      .   ' \\| | `.
                       / \\||| : ||| \
                     / _||||| -:- |||||- \
                       | | \\\ - / | |
                     | \_| ''\---/'' | |
                      \ .-\__ `-` ___/-. /
                   ___`. .' /--.--\ `. . __
                ."" '< `.___\_<|>_/___.' >'"".
               | | : `- \`.;`\ _ /`;.`/ - ` : | |
                 \ \ `-. \_ __\ /__ _/ .-` / /
         ======`-.____`-.___\_____/___.-`____.-'======
                            `=---='

         .............................................
                  佛祖保佑             永无BUG
          佛曰:
                  写字楼里写字间，写字间里程序员；
                  程序人员写程序，又拿程序换酒钱。
                  酒醒只在网上坐，酒醉还来网下眠；
                  酒醉酒醒日复日，网上网下年复年。
                  但愿老死电脑间，不愿鞠躬老板前；
                  奔驰宝马贵者趣，公交自行程序员。
                  别人笑我忒疯癫，我笑自己命太贱；
                  不见满街漂亮妹，哪个归得程序员？
         .............................................

*/
