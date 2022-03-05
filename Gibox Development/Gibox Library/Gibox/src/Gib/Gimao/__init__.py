"""
文件名称：cdmaoapi库
用处：获取/提交编程猫官方数据
优点：集合大量接口，简化大量requests步骤，就可获取资料！
不仅是获取，还可以与官方后台交互，如：回复评论，作品收藏，作品点赞等。
你可以用本库来开发更多有趣的功能哦！
开发者：SS_LiMgXn,冷鱼闲风
更新日期：2020.10.25
官方文档：http://doc.viyrs.com/cdmaoapi.html
"""

import requests
import json

SubmitCookie = ''

class GCodeMaoProgram(object):
    def Get(self, Url):
        """程序专用
        用来Get请求
        配有请求头"""
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }

        rr = requests.get(Url, headers=headers)
        rr.encoding = 'utf-8'
        rrr = rr.text
        return json.loads(rrr)

    def Submit(self, Url, Data, ID):
        """程序专用
        用来Post/Put/Patch请求
        配有请求头
        Cookie须自己设定"""
        if SubmitCookie == '':
            raise BcmapiError('Cookie值为空，请使用"cdmaoapi.submitCookie"设置cookie值！')
        headers = {'cookie': str(SubmitCookie),
                   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
        if ID == 1:
            return requests.post(Url, headers=headers, json=Data)
        elif ID == 2:
            return requests.put(Url, headers=headers)
        elif ID == 3:
            return requests.patch(Url, headers=headers)

class GCodeMaoUser(object):
    def __init__(self, GcmId):
        self.Program = GCodeMaoProgram()
        brr = self.Program.Get('https://api.codemao.cn/api/user/attention/me?user_id=' + str(GcmId))
        bId = []
        bName = []
        bAvatar = []
        for i in range(int(len(list(brr['data']['attentionList'])))):
            bId.append(brr['data']['attentionList'][i]['id'])
            bName.append(brr['data']['attentionList'][i]['nickname'])
            bAvatar.append(brr['data']['attentionList'][i]['avatar'])
        arr = self.Program.Get('https://api.codemao.cn/api/user/me/attention?user_id=' + str(GcmId))
        aId = []
        aName = []
        aAvatar = []
        if arr['code'] == 7001:  # 若为空
            pass
        else:
            for i in range(int(len(list(arr['data']['attentionList'])))):
                aId.append(arr['data']['attentionList'][i]['id'])
                aName.append(arr['data']['attentionList'][i]['nickname'])
                aAvatar.append(arr['data']['attentionList'][i]['avatar'])
        wrr = self.Program.Get(
            'https://api.codemao.cn/api/user/works/published?user_id=' + str(GcmId) + '&limit=100&types=1,3,5')
        wId = []
        wName = []
        wPreview = []
        wDescription = []
        if wrr['code'] == 7001:  # 若为空
            pass
        else:
            for i in range(int(len(list(wrr['data']['works'])))):
                wId.append(wrr['data']['works'][i]['work_id'])
                wName.append(wrr['data']['works'][i]['name'])
                wDescription.append(wrr['data']['works'][i]['description'])
                wPreview.append(wrr['data']['works'][i]['preview'])
        rr = self.Program.Get('https://api.codemao.cn/api/user/info/detail/' + str(GcmId))
        srr = self.Program.Get('https://api.codemao.cn/web/work-shops/' + str(GcmId) + '/participators')
        self.UserId = GcmId  # 用户Id
        self.UserAvatar = rr['data']['userInfo']['user']['avatar']  # 用户链接
        self.UserName = rr['data']['userInfo']['user']['nickname']  # 用户名称
        self.UserStudId = srr['subject_id']  # 用户工作室ID
        self.UserStudName = srr['name']  # 用户工作室名称
        self.UserStudLevel = srr['level']  # 用户工作室等级
        self.UserBenoId = bId  # 用户被关注资料
        self.UserBenoName = bName
        self.UserBenoAvatar = bAvatar
        self.UserAtteId = aId  # 用户关注资料
        self.UserAtteName = aName
        self.UserAtteAvatar = aAvatar
        self.__userWorkId = wId  # 隐藏的作品资料
        self.__userWorkName = wName
        self.__userWorkAvatar = wPreview
        self.__userWorkDesc = wDescription
        self.CoverWorkId = rr['data']['userInfo']['work']['id']  # 封面作品资料
        self.CoverWorkName = rr['data']['userInfo']['work']['name']
        self.CoverWorkAvatar = rr['data']['userInfo']['work']['preview']
        self.UserDesc = rr['data']['userInfo']['user']['description']  # 简介
        self.UserDoing = rr['data']['userInfo']['user']['doing']  # 我在做什么？
        self.UserViewTs = rr['data']['userInfo']['viewTimes']  # 浏览量
        self.UserPraiseTs = rr['data']['userInfo']['praiseTimes']  # 赞数
        self.UserForked = rr['data']['userInfo']['forkedTimes']  # 再创作数
        self.UserCollection = rr['data']['userInfo']['collectionTimes']  # 收藏数

    def GetWork(self):
        return {'WorkId': self.__userWorkId,
                'WorkName': self.__userWorkName,
                'WorkAvatar': self.__userWorkAvatar,
                'WorkDesc': self.__userWorkDesc
                }

class GBcmapiError(Exception):
    """Exception异常子类，用来显示cdmaoapi异常"""

    def __init__(self, msg):
        self.msg = msg
        Exception.__init__(self)

    def __str__(self):
        return self.msg

class GCodeMaoHomeWork:
    def __init__(self, WorkICode):
        self.Program = GCodeMaoProgram()
        code = {'新作喵喵看': 1, '点猫': 2, '动作': 16, '休闲': 15, '射击': 17, '艺术': 18, '冒险': 21, '学术': 19, '故事': 20}[str(WorkICode)]
        rr = self.Program.get(
            'https://api.codemao.cn/web/works/channels/' + str(code) + '/works?type=KITTEN&page=1&limit=10')
        zpid = []
        name = []
        description = []
        view_times = []
        praise_times = []
        preview = []
        userid = []
        nickname = []
        avatar_url = []
        for i in range(int(len(list(rr['items'])))):
            zpid.append(rr['items'][i]['id'])
            name.append(rr['items'][i]['name'])
            description.append(rr['items'][i]['description'])
            view_times.append(rr['items'][i]['view_times'])
            praise_times.append(rr['items'][i]['praise_times'])
            preview.append(rr['items'][i]['preview'])
            userid.append(rr['items'][i]['user']['id'])
            nickname.append(rr['items'][i]['user']['nickname'])
            avatar_url.append(rr['items'][i]['user']['avatar_url'])
        self.WorkId = zpid  # 作品资料
        self.WorkName = name
        self.WorkDesc = description
        self.WorkViewTs = view_times  # 浏览量
        self.WorkPraiTs = praise_times  # 赞数
        self.WorkAvatar = preview  # 图片
        self.WorkMakerId = userid  # 制作者资料
        self.WorkMakerName = nickname
        self.WorkMakerAvatar = avatar_url

class GCodeMaoWorks:
    def __init__(self, WorkID):
        self.Program = GCodeMaoProgram()
        self.WorkID = WorkID
        drr = get(
            'https://api.codemao.cn/web/discussions/' + str(
                WorkID) + '/comments?source=WORK&sort=-created_at&limit=20&offset=0')
        self.__data = drr
        rr = get('https://api.codemao.cn/web/works/' + str(WorkID))
        did = []
        dname = []
        dpreview = []
        ddescription = []
        dsubject_id = []
        dcontent = []
        for i in range(int(len(list(drr['items'])))):
            did.append(drr['items'][i]['id'])
            dname.append(drr['items'][i]['user']['id'])
            ddescription.append(drr['items'][i]['user']['nickname'])
            dpreview.append(drr['items'][i]['user']['avatar_url'])
            dsubject_id.append(drr['items'][i]['user']['subject_id'])
            dcontent.append(drr['items'][i]['content'])
        self.WorkName = rr['work_name']  # 作品名称
        self.WorkIntr = rr['work_introduction']  # 介绍
        self.WorkDesc = rr['operation_description']  # 操作介绍
        self.ViewTs = rr['view_times']  # 浏览
        self.PraiTs = rr['praise_times']  # 点赞
        self.CollTs = rr['collect_times']  # 收藏
        self.CommTs = rr['comment_times']  # 评论
        self.WorkAvatar = rr['preview']  # 图片
        self.MakerId = rr['user_info']['id']  # 制作者名称
        self.MakerAvatar = rr['user_info']['avatar']
        self.MakerName = rr['user_info']['nickname']
        self.MakerSign = rr['user_info']['signature']
        self.CommentId = did  # 评论资料
        self.CommentUserId = dname
        self.CommentUserName = ddescription
        self.CommentUserAvatar = dpreview
        self.CommentStudio = dsubject_id
        self.CommentContent = dcontent

    def GetSub(self, FID):
        """爬取子评论
        FID : 父评论Id"""
        rr = self.__data
        zpid = []
        name = []
        preview = []
        description = []
        subject_id = []
        content = []
        j = 0

        for i in range(20):
            if rr['items'][i]['id'] == str(FID):
                j = i
                break
        try:  # 若为空
            rr['items'][j]['replies']['total']
        except:
            return {'subId': None,
                    'userId': None,
                    'userAvatar': None,
                    'userName': None,
                    'userStudId': None,
                    'subContent': None
                    }

        for i in range(rr['items'][j]['replies']['total']):
            zpid.append(rr['items'][j]['replies']['items'][i]['id'])
            name.append(rr['items'][j]['replies']['items'][i]['reply_user']['id'])
            description.append(rr['items'][j]['replies']['items'][i]['reply_user']['nickname'])
            preview.append(rr['items'][j]['replies']['items'][i]['reply_user']['avatar_url'])
            subject_id.append(rr['items'][j]['replies']['items'][i]['reply_user']['subject_id'])
            content.append(rr['items'][j]['replies']['items'][i]['content'])
        return {'subId': zpid,
                'userId': name,
                'userAvatar': preview,
                'userName': description,
                'userStudId': subject_id,
                'subContent': content
                }

    def SubmitComment(self, Content):
        """使用Post请求提交评论
        content : 评论内容"""
        data = {'content': str(Content), 'rich_content': str(Content), 'source': 'WORK'}
        url = 'https://api.codemao.cn/web/discussions/' + str(self.WorkID) + '/comment'
        return self.Program.Submit(url, data, 1)

    def SubmitSub(self, fid, zid, content):
        """使用Post请求提交子评论
        content : 评论内容
        fid : 父(祖)评论Id
        zid : fid的子评论Id (此时fid是你的祖评论，zid是你回复的评论，若没有填0)"""
        data = {'content': str(content), 'parent_id': str(zid), 'source': 'WORK'}
        url = 'https://api.codemao.cn/web/discussions/' + str(self.WorkID) + '/comments/' + str(fid) + '/reply'
        return self.Program.Submit(url, data, 1)

    def SubmitCommentTZ(self, CommentId):
        """使用Put请求提交评论点赞
        plid : 评论id
        """
        data = ''
        url = 'https://api.codemao.cn/web/discussions/comments/' + str(CommentId) + '/liked'
        return self.Program.Submit(url, data, 2)


def CdmaoForumSubmit(title, content, ID):
    """使用Post请求进行论坛帖子发布
    content : 帖子内容（支持HTML）
    ID : 板块ID（1论坛广场，17热门活动，5你问我答，2积木编程乐园，10工作室，25师徒广场，26源码精灵，13NOC编程比赛，9作品秀，7灌水池塘，18Scratch专区，21休闲作品专区，19动作游戏专区，20射击游戏专区，23艺术作品专区，22学术作品专区，24工作室招新，12求素材，11Python乐园，3代码岛，6动漫小说，8我要提建议，4通天塔）
    title : 帖子标题"""
    data = {'content': str(content), 'title': str(title)}
    url = 'https://api.codemao.cn/web/forums/boards/' + str(ID) + '/posts'
    return submit(url, data, 1)


def CdmaoSeaWork(gjz):
    """使用Get请求进行作品搜索
    gjz : 搜索关键字"""
    zpid = []
    title = []
    userid = []
    nickname = []
    avatar_url = []
    subject_id = []
    work_shop_name = []
    work_shop_level = []

    rr = get(
        'https://api.codemao.cn/web/works/search?query=' + str(gjz) + '&offset=0&limit=20')
    for i in range(int(len(list(rr['items'])))):
        zpid.append(rr['items'][i]['id'])
        title.append(rr['items'][i]['name'])
        userid.append(rr['items'][i]['user']['id'])
        nickname.append(rr['items'][i]['user']['nickname'])
        avatar_url.append(rr['items'][i]['user']['avatar_url'])
        subject_id.append(rr['items'][i]['view_times'])
        work_shop_name.append(rr['items'][i]['praise_times'])
        work_shop_level.append(rr['items'][i]['preview'])
    return {'workId': zpid,
            'workName': title,
            'makerId': userid,
            'makerName': nickname,
            'makerAvatar': avatar_url,
            'viewTs': subject_id,
            'praiTs': work_shop_name,
            'workAvatar': work_shop_level}


def CdmaoSeaStud(gjz):
    """使用Get请求进行工作室搜索
    gjz : 搜索关键字"""
    rr = get('https://api.codemao.cn/web/work-shops/search?name=' + str(gjz) + '&limit=100')
    idd = []
    name = []
    avatar_url = []
    position = []
    level = []
    for i in range(int(rr['total'])):
        idd.append(rr['items'][i]['id'])
        name.append(rr['items'][i]['name'])
        avatar_url.append(rr['items'][i]['preview_url'])
        position.append(rr['items'][i]['description'])
        level.append(rr['items'][i]['level'])

    return {'studId': idd,
            'studName': name,
            'studAvatar': avatar_url,
            'studDesc': position,
            'studLevel': level,
            'totalStud': rr['total']}


def CdmaoForum(page):
    """
    使用get请求获取论坛板块前20条内容
    page : 板块值 （1论坛广场，17热门活动，5你问我答，2积木编程乐园，10工作室，25师徒广场，26源码精灵，13NOC编程比赛，9作品秀，7灌水池塘，18Scratch专区，21休闲作品专区，19动作游戏专区，20射击游戏专区，23艺术作品专区，22学术作品专区，24工作室招新，12求素材，11Python乐园，3代码岛，6动漫小说，8我要提建议，4通天塔）
    """
    zpid = []
    title = []
    content = []
    userid = []
    nickname = []
    avatar_url = []
    subject_id = []
    work_shop_name = []
    work_shop_level = []
    if page == 1:
        rr = get('https://api.codemao.cn/web/forums/posts/hots/all')
        rr = rr['items'][:21]
        idd = ','.join(rr)
        rr = get("https://api.codemao.cn/web/forums/posts/all?ids=" + idd)
    else:
        rr = get('https://api.codemao.cn/web/forums/boards/' + str(page) + '/posts')
    for i in range(20):
        zpid.append(rr['items'][i]['id'])
        title.append(rr['items'][i]['title'])
        content.append(rr['items'][i]['content'])
        userid.append(rr['items'][i]['user']['id'])
        nickname.append(rr['items'][i]['user']['nickname'])
        avatar_url.append(rr['items'][i]['user']['avatar_url'])
        subject_id.append(rr['items'][i]['user']['subject_id'])
        work_shop_name.append(rr['items'][i]['user']['work_shop_name'])
        work_shop_level.append(rr['items'][i]['user']['work_shop_level'])

    return {'postId': zpid,
            'postTitle': title,
            'postContent': content,
            'writerId': userid,
            'writerName': nickname,
            'writerAvatar': avatar_url,
            'writerStudId': subject_id,
            'writerStudName': work_shop_name,
            'writerStudLevel': work_shop_level}


def CdmaoSeaForum(gjz):
    """使用Get请求进行论坛搜索
    gjz : 搜索关键字"""
    zpid = []
    title = []
    userid = []
    nickname = []
    avatar_url = []
    subject_id = []
    work_shop_name = []
    work_shop_level = []

    rr = get(
        'https://api.codemao.cn/web/forums/posts/search?title=' + str(gjz) + '&limit=20')
    for i in range(int(len(list(rr['items'])))):
        zpid.append(rr['items'][i]['id'])
        title.append(rr['items'][i]['title'])
        userid.append(rr['items'][i]['user']['id'])
        nickname.append(rr['items'][i]['user']['nickname'])
        avatar_url.append(rr['items'][i]['user']['avatar_url'])
        subject_id.append(rr['items'][i]['user']['subject_id'])
        work_shop_name.append(rr['items'][i]['user']['work_shop_name'])
        work_shop_level.append(rr['items'][i]['user']['work_shop_level'])
    return {'postId': zpid,
            'postTitle': title,
            'writerId': userid,
            'writerName': nickname,
            'writerAvatar': avatar_url,
            'writerStudId': subject_id,
            'writerStudName': work_shop_name,
            'writerStudLevel': work_shop_level
            }


def CdmaoHomeCF():
    """首页轮播图获取"""
    rr = get('https://api.codemao.cn/web/banners/all?type=OFFICIAL')
    name = []
    preview = []
    description = []
    subject_id = []
    rrr = requests.get("https://api.codemao.cn/web/banners/all?type=OFFICIAL")
    rrr.encoding = 'utf-8'
    rrr = rrr.text
    for i in range(int(rrr.count('title'))):
        name.append(rr['items'][i]['title'])
        description.append(rr['items'][i]['target_url'])
        preview.append(rr['items'][i]['background_url'])
        subject_id.append(rr['items'][i]['small_background_url'])

    return {'cfName': name,  # 轮播图名称
            'cfBgUrl': description,  # 轮播图3个地址
            'cfBigBg': preview,
            'cfSmallBg': subject_id
            }


class CdmaoStudio:
    """工作室类，__init__参数：
    bcmid : 工作室id"""

    def __init__(self, bcmid):
        self.id = bcmid
        rr = get('https://api.codemao.cn/web/shops/' + str(bcmid) + '/users?limit=80&offset=0')
        idd = []
        name = []
        avatar_url = []
        position = []
        qq = []
        for i in range(int(rr['total'])):
            idd.append(rr['items'][i]['user_id'])
            name.append(rr['items'][i]['name'])
            avatar_url.append(rr['items'][i]['avatar_url'])
            position.append(rr['items'][i]['position'])
            qq.append(rr['items'][i]['qq'])
        rr = get('https://api.codemao.cn/web/shops/' + str(bcmid))
        self.studId = rr['id']
        self.studName = rr['name']
        self.studScore = rr['total_score']  # 工作室积分
        self.studAvatar = rr['preview_url']
        self.studLevel = rr['level']
        self.studDesc = rr['description']
        self.studMembersId = idd  # 成员资料
        self.studMembersName = name
        self.studMembersAvatar = avatar_url
        self.studMembersPos = position
        self.studMembersQQ = qq

    def get_Discussions(self):
        """获取工作室评论"""
        rr = get('https://api.codemao.cn/web/discussions/' + str(
            self.id) + '/comments?source=WORK_SHOP&sort=-created_at&limit=20&offset=0')
        idd = []
        nickname = []
        avatar_url = []
        position = []
        level = []
        content = []
        for i in range(int(rr['limit'])):
            idd.append(rr['items'][i]['id'])
            nickname.append(rr['items'][i]['user']['nickname'])
            avatar_url.append(rr['items'][i]['user']['avatar_url'])
            position.append(rr['items'][i]['user']['id'])
            level.append(rr['items'][i]['user']['subject_id'])
            content.append(rr['items'][i]['content'])
        return {'dId': idd,  # 评论资料
                'userName': nickname,
                'userAvatar': avatar_url,
                'userId': position,
                'userStudId': level,
                'dContent': content
                }

    def get_work(self, ysort):
        """获取工作室作品
        ysort : 排序方式，new最新 hot最火"""
        sort = {'new': '-audited_at,-id', 'hot': '-n_likes'}[str(ysort)]
        rr = get(
            'https://api.codemao.cn/web/works/subjects/' + str(self.id) + '/works?&offset=0&limit=100&sort=' + sort)
        zpid = []
        name = []
        view_time = []
        praise_times = []
        preview = []
        userid = []
        nickname = []
        avatar_url = []
        for i in range(int(rr['limit'])):
            zpid.append(rr['items'][i]['id'])
            name.append(rr['items'][i]['name'])
            view_time.append(rr['items'][i]['view_times'])
            praise_times.append(rr['items'][i]['praise_times'])
            preview.append(rr['items'][i]['preview'])
            userid.append(rr['items'][i]['user']['id'])
            nickname.append(rr['items'][i]['user']['nickname'])
            avatar_url.append(rr['items'][i]['user']['avatar_url'])

        return {'workId': zpid,
                'workName': name,
                'viewTs': view_time,
                'praiTs': praise_times,
                'workAvatar': preview,
                'makerId': userid,
                'makerName': nickname,
                'makerAvatar': avatar_url
                }

    def StudNewWork(self, zpid):
        """使用Post方法投稿作品
        zpid : 作品id"""
        data = {}
        url = 'https://api.codemao.cn/web/work_shops/works/contribute?id=' + str(self.id) + '&work_id=' + str(zpid)

        return submit(url, data, 1)

    def StudDeleteWork(self, zpid):
        """使用Post方法删除作品
        zpid : 作品id"""
        data = {}
        url = 'https://api.codemao.cn/web/work_shops/works/remove?id=' + str(self.id) + '&work_id=' + str(zpid)
        return submit(url, data, 1)

    def StudSet(self, name, preview_url, description):
        """设置工作室资料
        name : 名称
        preview_url : 工作室图片
        description : 工作室简介"""
        data = {'id': str(self.id), 'name': str(name), 'preview_url': str(preview_url), 'description': str(description)}
        url = 'https://api.codemao.cn/web/work_shops/update'
        return submit(url, data, 1)


class CdmaoForumIn:
    """论坛类，__init__参数：
    ltid : 帖子id"""

    def __init__(self, ltid):
        self.ltid = ltid
        rr = get('https://api.codemao.cn/web/forums/posts/' + str(ltid) + '/details')
        self.writerId = rr['user']['id']
        self.writerName = rr['user']['nickname']
        self.writerAvatar = rr['user']['avatar_url']
        self.writerStudId = rr['user']['subject_id']
        self.writerStudName = rr['user']['work_shop_name']
        self.writerStudLevel = rr['user']['work_shop_level']
        self.postTitle = rr['title']
        self.postBoard = rr['board_name']
        self.postBoardId = rr['board_id']
        self.postView = rr['n_views']
        self.content = rr['content']

    def SubmitComment(self, content):
        """使用Post请求提交评论
        content : 评论内容"""
        data = {'content': str(content)}
        url = 'https://api.codemao.cn/web/forums/posts/' + str(self.ltid) + '/replies'
        return submit(url, data, 1)

    def SubmitSub(self, fid, zid, content):
        """使用Post请求提交子评论
        content : 评论内容
        fid : 父(祖)评论Id
        zid : fid的子评论Id (此时fid是你的祖评论，zid是你回复的评论，若没有填0)"""
        data = {'content': str(content), 'parent_id': str(zid)}
        url = 'https://api.codemao.cn/web/forums/replies/' + str(fid) + '/comments'
        return submit(url, data, 1)
