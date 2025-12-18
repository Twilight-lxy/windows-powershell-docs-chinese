---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/set-appvclientconfiguration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AppvClientConfiguration
---

# 设置 AppVClient 配置

## 摘要
将配置设置应用到 App-V 客户端上。

## 语法

```
Set-AppvClientConfiguration [-AllowHighCostLaunch <Boolean>] [-AutoLoad <UInt32>]
 [-CertFilterForClientSsl <String>] [-EnablePackageScripts <Boolean>] [-EnablePublishingRefreshUI <Boolean>]
 [-IntegrationRootGlobal <String>] [-IntegrationRootUser <String>] [-LocationProvider <String>]
 [-MigrationMode <Boolean>] [-PackageInstallationRoot <String>] [-PackageSourceRoot <String>]
 [-RequirePublishAsAdmin <Boolean>] [-ReestablishmentInterval <UInt32>] [-ReestablishmentRetries <UInt32>]
 [-ReportingDataBlockSize <UInt32>] [-ReportingDataCacheLimit <UInt32>] [-ReportingEnabled <Boolean>]
 [-ReportingInterval <UInt32>] [-ReportingRandomDelay <UInt32>] [-ReportingServerURL <String>]
 [-ReportingStartTime <UInt32>] [-RoamingFileExclusions <String>] [-RoamingRegistryExclusions <String>]
 [-SharedContentStoreMode <Boolean>] [-VerifyCertificateRevocationList <Boolean>]
 [-ExperienceImprovementOptIn <Boolean>] [-ProcessesUsingVirtualComponents <String[]>]
 [-EnableDynamicVirtualization <Boolean>] [-IgnoreLocationProvider <Boolean>] [-SupportBranchCache <Boolean>]
 [<CommonParameters>]
```

## 描述
`Set-AppvClientConfiguration` cmdlet 用于将配置设置应用到 Microsoft 应用虚拟化（App-V）客户端。每个参数代表一个可以更改的设置。

## 示例

### 示例 1：设置客户端配置参数
```
PS C:\> Set-AppvClientConfiguration -parameter1 "parameterVal1"
```

这个示意图示例设置了一个特定的客户端配置参数。

## 参数

### -AllowHighCostLaunch
指定是否在通过计量型网络连接（例如4G）连接的Windows 8计算机上启动虚拟化应用程序。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AutoLoad
指定App-V应如何在特定计算机上自动加载新包。该参数的可接受值包括：

- 0 for None
- 1 for Previously used
- 2 for All

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CertFilterForClientSsl
指定证书存储中有效证书的路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnableDynamicVirtualization
指定是否启用动态虚拟化功能。动态虚拟化允许支持的Shell扩展程序、浏览器辅助对象（Browser Helper Objects）以及Active X控件在虚拟环境中运行，并与虚拟应用程序一起使用。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnablePackageScripts
指定是否启用配置文件包清单中定义的脚本的运行功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnablePublishingRefreshUI
指定是否为客户端启用发布刷新进度条功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ExperienceImprovementOptIn
指定是选择参与（$True）还是不参与（$False）客户体验改进计划。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IgnoreLocationProvider
指定是否强制客户端忽略“Location Provider”路径，而使用“Package Source Root”。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IntegrationRootGlobal
指定用于创建与当前版本的全球发布软件包相关联的符号链接的位置。所有虚拟应用程序扩展（例如快捷方式以及文件类型关联）都会使用此路径。如果您没有指定路径，在发布软件包时将不会使用符号链接。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IntegrationRootUser
指定用于创建与当前版本的用户专属发布包相关联的符号链接的位置。所有虚拟应用程序扩展（例如快捷方式及文件类型关联）都会使用此路径。如果您没有指定路径，在发布该包时将不会使用符号链接。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LocationProvider
指定 IAppvPackageLocationProvider 接口的一个兼容实现的类标识符（CLSID）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MigrationMode
指定是否使用迁移模式。迁移模式允许App-V客户端控制通过早期版本的App-V发布的程序包的快捷方式（shortcuts）和文件传输协议（FTAs）。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PackageInstallationRoot
指定用于安装所有新应用程序和更新文件的目录。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PackageSourceRoot
指定一个值，该值会覆盖用于下载包内容的源位置。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ProcessesUsingVirtualComponents
指定一个进程路径列表，这些路径的进程可以作为使用动态虚拟化的候选对象，用于支持相应的shell扩展、浏览器辅助对象（browser helper objects）和ActiveX控件。该参数可以包含通配符字符。只有那些完整路径与列表中的某个条目匹配的进程才能使用动态虚拟化功能。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReestablishmentInterval
指定在尝试重新建立已中断的会话之间等待的秒数。该参数的可接受值为：0到3600之间的任意数值。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReestablishmentRetries
指定重新尝试已断开的会话的次数。该参数的可接受值为：0 到 99 之间的任意整数。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportingDataBlockSize
指定用于向服务器传输上传请求报告的最大数据量（以字节为单位）。这有助于避免在日志文件体积过大时发生永久性的传输失败。该参数的可接受取值范围是：1024 到无限大之间。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportingDataCacheLimit
指定用于存储报告信息的XML缓存的最大大小（以兆字节MB为单位）。该大小指的是内存中的缓存空间。当达到上限时，日志文件将会被替换。此参数的可接受取值范围是：0到1024之间。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportingEnabled
指定是否允许客户端向报告服务器返回信息。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportingInterval
指定客户端用于将数据重新发送到报告服务器的重试间隔时间。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportingRandomDelay
指定数据发送到报告服务器的最大延迟时间（以分钟为单位）。当计划任务启动时，客户端会生成一个介于 0 和 *ReportingRandomDelay* 之间的随机延迟值，并在等待指定的时间长度后才会发送数据。这样可以有助于避免服务器上的数据冲突。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportingServerURL
指定客户端信息在报告服务器上保存的位置。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportingStartTime
指定客户端开始向报告服务器发送数据的时间。该参数的可接受值为：0到23之间的整数，对应于一天中的小时数。默认情况下，*ReportingStartTime*从当天的晚上10点（即22:00）开始计算。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RequirePublishAsAdmin
指定非特权用户是否可以发布已注册的App-V软件包。

此参数自 App-V 5.0 SP3 版本起开始适用。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RoamingFileExclusions
指定相对于 `%userprofile%` 的文件路径，这些路径不会随用户的个人资料一起迁移。例如：`'desktop;my pictures'`。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RoamingRegistryExclusions
指定那些不会随用户配置文件一起迁移的注册表路径，例如 `‘software\\classes;software\\clients’`。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SharedContentStoreMode
指定是否不将流式传输的包内容保存到本地硬盘上。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SupportBranchCache
指定是否启用分支缓存功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VerifyCertificateRevocationList
指定在使用 HTTPS 进行数据传输之前是否需要验证服务器证书的吊销状态。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.AppvAgent.AppvClientConfiguration

## 输出

### Microsoft.AppvAgent.AppvClientConfiguration
此cmdlet返回一个对象，该对象以两列表格的形式显示。第一列包含具体的配置信息，第二列包含相应的当前值。

如果传递了名称/值选项，该cmdlet会返回相同的二维表格，但仅包含所请求的配置信息。

## 备注
* Before applying new configuration, the cmdlet checks if Group Policy already owns any configuration by checking `HKLM\Software\Policies\Microsoft\Application Virtualization`. If any of the provided configuration is in the Group Policy registry node, the cmdlet fails. If Group Policy does not own any of the supplied configuration, the settings are written to the `HKLM\Software\Microsoft\AppV` registry node. If the cmdlet is trying to modify multiple settings, if any are owned by Group Policy, the whole operation fails.
* In the case where Group Policy owns the setting, the cmdlet returns the following error: The App-V configuration trying to be modified is being managed by Group Policy. The cmdlet cannot perform the modification. An error code is returned.
* If any of the provided configuration are not valid App-V Client settings, the cmdlet fails and returns an error.
* The cmdlet checks that you have permissions to perform the specific action. If not, the cmdlet returns an error.
* If the action to set a property fails, the cmdlet returns an error.

## 相关链接

[Get-AppvClientConfiguration](./Get-AppvClientConfiguration.md)

