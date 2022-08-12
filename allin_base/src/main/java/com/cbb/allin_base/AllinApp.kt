package com.cbb.allin_base

import android.app.Activity
import android.app.Application
import android.content.Context
import com.blankj.utilcode.util.AppUtils
import com.blankj.utilcode.util.Utils

/**
 * @author cbb
 * Application 基类
 */
class AllinApp:Application() {
    companion object{
        var appIsFront = false//APP 位于前台
    }
    override fun attachBaseContext(base: Context?) {
        super.attachBaseContext(base)
    }
    override fun onCreate() {
        super.onCreate()
        Utils.init(this)
        AppUtils.registerAppStatusChangedListener(object :Utils.OnAppStatusChangedListener{
            override fun onForeground(activity: Activity?) {
                appIsFront = true
            }

            override fun onBackground(activity: Activity?) {
                appIsFront = false
            }
        })
    }
}