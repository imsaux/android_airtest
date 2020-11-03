
    def _banner_detail(self):
        # 轮播图详情
        self.poco("android.widget.ImageView").click()
        keyevent("BACK")
        _v = self.poco("android.widget.LinearLayout").offspring("com.sgcc.grsg.app:id/root_view").offspring("com.sgcc.grsg.app:id/navigation").offspring("com.sgcc.grsg.app:id/tv_navigatio_title")
        _v.wait_for_appearance()
        assert_equal(_v.get_text(), '培育创新', '返回培育创新首页正常')
