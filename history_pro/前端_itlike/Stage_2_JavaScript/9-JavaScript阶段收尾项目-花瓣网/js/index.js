/**
 * Created by xiaoming
 * 创建日期: 2019/4/5
 * 创建时间: 13:57
 */

(function (window) {
    // 1调用选项卡函数
    tab();

    // 2动态创建 元素
    autoCreateImg();

    setTimeout(function () {
        // 3瀑布流的布局
        waterFull("dom_pull", "box");

    }, 200);

    // 4.监听窗口的滚动
    window.onscroll = function () {
        if (checkWillLoadImage()) {
            autoCreateImg();
            waterFull("dom_pull", "box");
        }
        // console.log(112);
          // 4.2 判断是否吸顶
        var scrollTop =scroll().top;
        if(scrollTop >=150){
            $('top_nav').style.display = "block";
            $('elevator').style.display = "block";
        }else{
            $('top_nav').style.display = "none";
            $('elevator').style.display = "none";
        }

        // 4.4. 滚回顶部
        $('elevator').onclick = function () {
            buffer(document.documentElement, {scrollTop: 0}, null);
        }
    };
    // 5监听点击按钮
    // 拿到登录按钮
    $("login").onclick = function () {
       $("mask").style.display = "block";
    };
    $("close_btn").onclick = function () {
        $("mask").style.display = "none";
    };

    // 6 广告轮播,自动的
    bannerAutoPlay();


})(window);

/**
 * 自动轮播
 */
function bannerAutoPlay() {
   // 1. 获取所有的li标签
   var lis = $("slider_banner").getElementsByTagName("li");
   var index = 0;
   // 2. 开始定时器
   setInterval(function () {
       // 2.1 改变透明度
       for(var i=0; i<lis.length; i++){
           var singerLi = lis[i];
           buffer(singerLi, {opacity: 0}, null);
       }
       buffer(lis[index], {opacity: 1}, null);

       // 2.2 索引++
       index++;
       if(index === lis.length){
           index = 0;
       }
   }, 2000);
}


function autoCreateImg() {
    // 1.数据
    var json = [
        {txt: '当我们正在为生活疲于奔命的时候，生活已经离我们而去。——约翰·列侬', pic: 'images/0.jpg'},
        {txt: '活在世上，不必什么都知道，只知道最好的就够了。——王小波', pic: 'images/1.jpg'},
        {txt: '谁给我一滴水，我便回报他整个大海。——华梅', pic: 'images/self/12.jpg'},
        {txt: '世界上任何书籍都不能带给你好运，但是它们能让你悄悄变成你自己。——黑塞', pic: 'images/2.jpg'},
        {txt: '很多人不需要再见，只是路过而已。——《彼岸花》', pic: 'images/3.jpg'},
        {txt: '人生最困难的三件事：保守秘密，忘掉所受的创伤，充分利用余暇。——吉罗', pic: 'images/4.jpg'},
        {txt: '有些人是离开后，才会发觉那个人是最喜欢的。——《东邪西毒》', pic: 'images/5.jpg'},
        {txt: '我总是在日暮时分,书影与书影之间,宁静的悲哀里,最想念你。——亦舒', pic: 'images/6.jpg'},
        {txt: '再长的路，一步步地能走完，再短的路，不迈开双脚也无法到达。', pic: 'images/7.jpg'},
        {txt: '哪里会有人喜欢孤独，不过是不喜欢失望。——村上春树', pic: 'images/8.jpg'},
        {txt: '人时已尽，人世很长，我在中间，应当休息。——顾城', pic: 'images/9.jpg'},
        {txt: '信任的深浅，不在于会不会对你笑，而在于愿不愿意在你面前哭。', pic: 'images/10.jpg'},
        {txt: '有一种旅行，不为跋涉千里的向往，只为漫无目的的闲逛，不为人山人海的名胜，只为怡然自乐的街景...', pic: 'images/11.jpg'},
        {txt: '人都会孤独，但唯独他，可以越过这尘世的热闹，一眼明白这世间所有的繁华不过是他身边的过眼云烟。', pic: 'images/12.jpg'},
        {txt: '不乱于心，不困于情。不畏将来，不念过往。如此，安好。', pic: 'images/13.jpg'},
        {txt: '每一个人都需要这样一个朋友：当以为自己再也笑不出来的时候，他能让你开怀大笑！', pic: 'images/14.jpg'},
        {txt: '咖啡苦与甜，不在于怎么搅拌，而在于是否放糖；', pic: 'images/15.jpg'},
        {txt: '其实我不是一定要等你，只是等上了，就等不了别人了。——《朝露若颜》', pic: 'images/16.jpg'},
        {txt: '一切都是瞬间，一切都会过去，一切过去了的都会变成亲切的怀念。——普希金', pic: 'images/17.jpg'},
        {txt: '多少人曾爱慕你年轻时的容颜，可知谁愿承受岁月无情的变迁', pic: 'images/18.jpg'},
        {txt: '不在任何东西面前失去自我，哪怕是教条，哪怕是别人的目光，哪怕是爱情。——《成为简·奥斯汀》', pic: 'images/19.jpg'},
        {txt: '你如果认识从前的我，也许你会原谅现在的我。——张爱玲', pic: 'images/20.jpg'},
        {txt: '简约不是少，而是没有多余。足够也不是多，而是刚好你在。', pic: 'images/21.jpg'},
        {txt: '若只是喜欢 何必夸张成爱。——林夕', pic: 'images/22.jpg'},
        {txt: '梦里出现的人，醒来时就该去见她，生活就是这么简单。——《新桥恋人》', pic: 'images/23.jpg'},
        {txt: '与众不同的你是幸运的，何必让自己变得与别人一样。', pic: 'images/24.jpg'},
        {txt: '阳光温热，岁月静好，你还不来，我怎敢老。', pic: 'images/25.jpg'},
        {txt: '一个人知道自己为什么而活，就能忍受任何生活。——尼采', pic: 'images/26.jpg'},
        {txt: '我们已经出发了太久，以至于我们忘了为什么要出发。——纪伯伦', pic: 'images/27.jpg'},
        {txt: '水来，我在水中等你；火来，我在灰烬中等你。——《你是我的独家记忆》', pic: 'images/28.jpg'},
        {txt: '天下就没有偶然，那不过是化了妆的，戴了面具的必然。——钱钟书', pic: 'images/29.jpg'},
        {txt: '土地是以它的肥沃和收获而被估价的；才能也是土地，不过它生产的不是粮食，而是真理。', pic: 'images/30.jpg'},
        {txt: '土地是以它的肥沃和收获而被估价的；才能也是土地，不过它生产的不是粮食，而是真理。', pic: 'images/30.jpg'},
        {txt: '如果只能滋生瞑想和幻想的话，即使再大的才能也只是砂地或盐池，那上面连小草也长不出来的。 —— 别林斯基', pic: 'images/31.jpg'},
        {txt: '谁给我一滴水，我便回报他整个大海。——华梅', pic: 'images/self/5.jpg'},
        {txt: '我需要三件东西：爱情友谊和图书。然而这三者之间何其相通！炽热的爱情可以充实图书的内容，图书又是人们最忠实的朋友。 —— 蒙田', pic: 'images/32.jpg'},
        {txt: '时间是一切财富中最宝贵的财富。 —— 德奥弗拉斯多', pic: 'images/33.jpg'},
        {txt: '谁给我一滴水，我便回报他整个大海。——华梅', pic: 'images/self/6.jpg'},
        {txt: '世界上一成不变的东西，只有“任何事物都是在不断变化的”这条真理。 —— 斯里兰卡', pic: 'images/34.jpg'},
        {txt: '真正的科学家应当是个幻想家；谁不是幻想家，谁就只能把自己称为实践家。 —— 巴尔扎克', pic: 'images/35.jpg'},
        {txt: '爱情原如树叶一样，在人忽视里绿了，在忍耐里露出蓓蕾。 —— 何其芳', pic: 'images/36.jpg'},
        {txt: '如果你浪费了自己的年龄，那是挺可悲的。因为你的青春只能持续一点儿时间——很短的一点儿时间。 —— 王尔德', pic: 'images/37.jpg'},
        {txt: '我读的书愈多，就愈亲近世界，愈明了生活的意义，愈觉得生活的重要。 —— 高尔基', pic: 'images/38.jpg'},
        {txt: '要使别人喜欢你，首先你得改变对人的态度，把精神放得轻松一点，表情自然，笑容可掬，这样别人就会对你产生喜爱的感觉了。——卡耐基', pic: 'images/39.jpg'},
        {txt: '谁给我一滴水，我便回报他整个大海。——华梅', pic: 'images/40.jpg'},
        {txt: '君子不镜于水，而镜于人。镜于水，见面之容，镜于人，则知吉与凶。——墨翟', pic: 'images/self/1.jpg'},
        {txt: '谁给我一滴水，我便回报他整个大海。——华梅', pic: 'images/self/3.jpg'},
        {txt: '君子不镜于水，而镜于人。镜于水，见面之容，镜于人，则知吉与凶。——墨翟', pic: 'images/self/4.jpg'},
        {txt: '谁给我一滴水，我便回报他整个大海。——华梅', pic: 'images/self/11.jpg'},
        {txt: '一个人至少拥有一个梦想，有一个理由去坚强。', pic: 'images/self/13.jpg'},
        {txt: '君子在下位则多谤，在上位则多誉；小人在下位则多誉，在上位则多谤。——柳宗元', pic: 'images/41.jpg'},
        {txt: '你若要喜爱你自己的价值，你就得给世界创造价值。——歌德', pic: 'images/42.jpg'},
        {txt: '时间会刺破青春表面的彩饰，会在美人的额上掘深沟浅槽；会吃掉稀世之珍！天生丽质，什么都逃不过他那横扫的镰刀。——莎士比亚', pic: 'images/43.jpg'},
        {txt: '如果我们想交朋友，就要先为别人做些事——那些需要花时间、体力、体贴、奉献才能做到的事。——卡耐基', pic: 'images/44.jpg'},
        {txt: '原谅敌人要比原谅朋友容易。——狄尔治夫人', pic: 'images/45.jpg'},
        {txt: '君子不镜于水，而镜于人。镜于水，见面之容，镜于人，则知吉与凶。——墨翟', pic: 'images/46.jpg'},
        {txt: '一个人的真正伟大之处就在于他能够认识到自己的渺小。——保罗', pic: 'images/47.jpg'},
        {txt: '有谦和、愉快、诚恳的态度，而同时又加上忍耐精神的人，是非常幸运的。——塞涅卡', pic: 'images/48.jpg'},
        {txt: '一个人至少拥有一个梦想，有一个理由去坚强。心若没有栖息的地方，到哪里都是在流浪。——三毛', pic: 'images/49.jpg'},
        {txt: '谁给我一滴水，我便回报他整个大海。——华梅', pic: 'images/self/2.jpg'},
        {txt: '艺术是什么？艺术是感情的表露，艺术使用的是一种人人都能理解的语言。——毛姆', pic: 'images/50.jpg'},
        {txt: '普通的艺术家模仿别人的作品,伟大的艺术家窃取别人的灵感。——乔布斯', pic: 'images/51.jpg'},
        {txt: '艺术向来都是要投入整个身心的事情，因此，艺术归根结底都是悲剧性的。——卡夫卡', pic: 'images/52.jpg'},
        {txt: ' 艺术并不是真理，艺术是谎言，然而这种谎言能教育我们去认识真理。美术是揭示真理的谎言。——毕加索 ', pic: 'images/53.jpg'},
        {txt: '别人的痛苦才是艺术的源泉。而你去受苦，只会成为别人的艺术源泉——王小波 ', pic: 'images/54.jpg'},
        {txt: '没有什么不朽的，包括艺术本身。唯一不朽的，是艺术所传递出来的对人和世界的理解——梵高 ', pic: 'images/55.jpg'},
        {txt: '大艺术家即便错，也会错出魅力来。好像王尔德说过‘在艺术中只有美丑而无所谓对错’。——余秋雨', pic: 'images/56.jpg'},
        {txt: '通常情况下，选择献身艺术的人，都曾自视与众不同。然而他很快会发现，自己的艺术、自己的与众不同，往往就扎根在与所有人的相似中。——阿尔贝·加缪', pic: 'images/57.jpg'},
        {txt: '伟大的艺术家所看到的，从来都不是世界的本来面目。一旦他看透了，他就不再是艺术家。——王尔德', pic: 'images/58.jpg'},
        {txt: '没有一个艺术家平日一天二十四小时始终是艺术家的，艺术家创造的重要一切，恒久的一切，总是只在罕有的充满灵性感的时刻完成的。——斯蒂芬·茨威格', pic: 'images/59.jpg'},
        {txt: '凡是艺术家都须有一半是诗人，一半是匠人。——朱光潜', pic: 'images/60.jpg'},
        {txt: '一个为艺术而艺术的人，常常从最不重要和最平凡的形象中获得最大的乐趣。——阿瑟·柯南·道尔', pic: 'images/61.jpg'},
        {txt: '生活安乐时，创作绝望之诗；生活不如意时，写出生之喜悦。——太宰治', pic: 'images/62.jpg'},
        {txt: '女人要有一间属于自己的小屋，一笔属于自己的薪金，才能真正拥有创作的自由。——伍尔夫', pic: 'images/63.jpg'},
        {txt: '年轻的时候，我们总是会将自己的创作冲动误解为创作才能。——钱钟书', pic: 'images/64.jpg'},
        {txt: '熟才能生巧。写过一遍，尽管不象样子，也会带来不少好处。不断地写作才会逐渐摸到文艺创作的底。', pic: 'images/65.jpg'},
        {txt: '', pic: 'images/66.jpg'},
        {txt: '没有收拾残局的能力，就别放纵善变的情绪', pic: 'images/67.jpg'},
        {txt: '不是井里没有水，而是你挖的不够深', pic: 'images/68.jpg'},
        {txt: '把现在的工作做好，才能幻想将来的事情，专注于眼前的事情，对于尚未发生的事情而陷入无休止的忧虑之中', pic: 'images/69.jpg'},
        {txt: '永远别放弃自己，哪怕所有人都放弃了你', pic: 'images/70.jpg'},
        {txt: '将来的你一定会感谢现在拼命的自己', pic: 'images/71.jpg'},
        {txt: '谁给我一滴水，我便回报他整个大海。——华梅', pic: 'images/self/7.jpg'},
        {txt: '谁给我一滴水，我便回报他整个大海。——华梅', pic: 'images/self/9.jpg'},
        {txt: '谁给我一滴水，我便回报他整个大海。——华梅', pic: 'images/self/10.jpg'}, {txt: '你的假装努力，欺骗的只有你自己', pic: 'images/72.jpg'},
        {txt: '多数的错失，是因为不坚持，不努力，不挽留，然后催眠自己说一切都是命运', pic: 'images/73.jpg'},
        {txt: '与其抱怨，不如改变。', pic: 'images/74.jpg'},
        {txt: '每一场爱情，都是为了举着灯，和自己相似身影的人相逢。', pic: 'images/75.jpg'},
        {txt: '只有做强势的女人，才能拥有强势的命运。', pic: 'images/76.jpg'},
        {txt: '命运要你成长的时候，总会安排一些让你不顺心的人或事刺激你　', pic: 'images/77.jpg'},
        {txt: '成长是一场和自己的比赛，不要担心别人会做得比你好，你只需要每天都做得比前一天好就可以了。', pic: 'images/78.jpg'},
        {txt: '机遇对于有准备的头脑有特别的亲和力。　', pic: 'images/79.jpg'},
        {txt: '不求与人相比，但求超越自己，要哭就哭出激动的泪水，要笑就笑出成长的性格！　', pic: 'images/80.jpg'},
        {txt: '一个人只有亲眼看到自己伤疤的时候才知道什么是痛，什么是对与错。', pic: 'images/81.jpg'},
        {txt: '这世界的大多数事情，不是稍微努力就可以搞定', pic: 'images/82.jpg'},
        {txt: '想要体面生活，又觉得打拼辛苦；想要健康身体，又无法坚持运动。', pic: 'images/83.jpg'},
        {txt: '谁给我一滴水，我便回报他整个大海。——华梅', pic: 'images/self/8.jpg'},
        {txt: '一定不要把别人都当傻子，事实上，所有你能遇到的人都比你聪明。', pic: 'images/84.jpg'},
        {txt: '改变自己，是自救；影响别人，是救人。', pic: 'images/85.jpg'},
        {txt: '选一个方向，定一个时间，剩下的只管努力与坚持', pic: 'images/86.jpg'},
        {txt: '不飞则已，一飞冲天；不鸣则已，一鸣惊人。', pic: 'images/87.jpg'},
        {txt: '我终生的等待，换不来你刹那的凝眸。', pic: 'images/88.jpg'},
        {txt: '只要有坚强的意志力，就自然而然地会有能耐、机灵和知识。', pic: 'images/89.jpg'},
        {txt: '不求与人相比，但求超越自己，要哭就哭出激动的泪水，要笑就笑出成长的性格！', pic: 'images/90.jpg'},
        {txt: '忘记昨天，直面今天，迎接明天', pic: 'images/91.jpg'},
        {txt: '善用内在潜能，你就是走运的人。', pic: 'images/92.jpg'},
        {txt: '命不能争，运可以造，弱者认命，强者抗命，能者求命，智者造命', pic: 'images/93.jpg'},
        {txt: '珍惜今天的拥有，明天才会富有', pic: 'images/94.jpg'},
        {txt: '以爱之心做事，感恩之心做人。', pic: 'images/95.jpg'},
        {txt: '、善用内在潜能，你就是走运的人。', pic: 'images/96.jpg'},
        {txt: '你一定不要做丑恶的人，但是世态炎凉，你也别太善良！马善被人骑，人善被人欺，过于善良就是一', pic: 'images/97.jpg'},
        {txt: '你们应该培养对自己，对自己的力量的信心，百这种信心是靠克服障碍，培养意志和锻炼意志而获得的。', pic: 'images/98.jpg'},
        {txt: '只要有坚强的意志力，就自然而然地会有能耐、机灵和知识。', pic: 'images/99.jpg'},
        {txt: '不求与人相比，但求超越自己，要哭就哭出激动的泪水，要笑就笑出成长的性格！', pic: 'images/100.jpg'}
    ], str, txt, pic, htmlStr;
    // 1.2遍历数组
    for (var i = 0; i < 115; i++) {
        // 1.2.0获取复标签的文本
        str = $("dom_pull").innerHTML;
        // 1.2.1quchu 取出图片地址的文字
        txt = json[i].txt;
        pic = json[i].pic;

// 1.2.2创建HTML字标签
        htmlStr = "                    <div class=\"box\">\n" +
            "                        <div class=\"pic\">\n" +
            "                            <img src=" + pic + " alt=\"\">\n" +
            "                            <!--蒙版-->\n" +
            "                            <div class=\"cover\"></div>\n" +
            "                        </div>\n" +
            "                        <p>" + txt + "</p>\n" +
            "<!--                        按钮-->\n" +
            "                        <div class=\"btn-box\">\n" +
            "                            <a href=\"#\" class=\"collect\">采集</a>\n" +
            "                            <a href=\"#\" class=\"like\">\n" +
            "                                <span class=\"heart\">\n" +
            "\n" +
            "                                </span>\n" +
            "                            </a>\n" +
            "                        </div>\n" +
            "                    </div>";

        htmlStr = "<div class='box'>" +
            "<div class='pic'>" +
            "<img src=" + pic + " alt=''>" +
            "<div class='cover'></div>" +
            "</div>" +
            "<p>" + txt + "</p>" +
            "<div class='btn-box' style='display: none'>" +
            "<a href='' class='collect'>采集</a>" +
            "<a href='' class='like'>" +
            "<span class='heart'></span>" +
            "</a></div></div>";

        // console.log(htmlStr);
        // 1.2.3拼接
        str += htmlStr;
        $("dom_pull").innerHTML = str;

        // 绑定事件
        var wrapBox = $("dom_pull").getElementsByClassName("box");
        var wrappic = $("dom_pull").getElementsByClassName("pic");


        // 监听鼠标的进入和离开
        // 先来一个循环

        for (var j = 0; j < wrapBox.length; j++) {

            wrapBox[j].onmouseover = function () {
                this.childNodes[2].style.display = "block";
            };

            wrapBox[j].onmouseout = function () {
                this.childNodes[2].style.display = "none";
            };

            wrappic[j].onmouseover = function () {
                this.childNodes[1].style.display = "block";
            };

            wrappic[j].onmouseout = function () {
                this.childNodes[1].style.display = "none";
            }
        }
    }

}

function tab() {
    // 1获取需要的标签
    var allLis = $("tab_header").getElementsByTagName("li");
    var doms = $("tab_content").getElementsByClassName("dom");
    var lastOne = 0;
    // 遍历监听,排他处理
    for (var i = 0; i < allLis.length; i++) {
        var li = allLis[i];
        (function (i) {
            li.onmousedown = function () {
                // 1清除样式
                allLis[lastOne].className = "";
                doms[lastOne].style.dispaly = "none";
                // 设置选中
                this.className = "current";
                doms[i].style.dispaly = "block";
                // 3fuzhi赋值
                lastOne = i;
            }
        })(i);

        // 闭包中,后面的括号放入i,就执行i次
    }
    // console.log(allLis);
    // console.log(doms);
}

function $(id) {
    return typeof id === "string" ? document.getElementById(id) : null;
}


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
