---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_BackgroundTask.cdxml-help.xml
Module Name: AppBackgroundTask
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appbackgroundtask/get-appbackgroundtask?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AppBackgroundTask
---

# Get-AppBackgroundTask

## 摘要
获取后台任务信息。

## 语法

```
Get-AppBackgroundTask [-PackageFamilyName <String>] [-IncludeResourceUsage] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-AppBackgroundTask` cmdlet 用于获取由 `PackageFamilyName` 参数指定的任务的背景任务信息。背景任务代表应用程序执行某些操作（例如下载文件）。要获取背景任务信息，必须具有管理员权限。

## 示例

### 示例 1：显示后台任务
```
PS C:\> Get-AppBackgroundTask -PackageFamilyName "Microsoft.BingSports_8wekyb3d8bbwe"
```

此命令会显示属于 Microsoft.BingSports_8wekyb3d8bbwe 包系列的已注册后台任务。

### 示例 2：显示带有资源使用数据的后台任务
```
PS C:\> Get-AppBackgroundTask -PackageFamilyName "Microsoft.BingSports_8wekyb3d8bbwe" -IncludeResourceUsage
```

此命令会显示属于 Microsoft.BingSports_8wekyb3d8bbwe 包系列的已注册后台任务，包括详细的资源使用信息。

### 示例 3：显示用户的所有后台任务
```
PS C:\> Get-AppBackgroundTask
```

这个命令会显示当前用户注册的所有后台任务。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值是本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IncludeResourceUsage
表示该 cmdlet 会显示后台任务的详细资源使用数据。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: iru

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PackageFamilyName
指定要显示后台任务信息的软件包系列名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: pfn

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时执行的操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance# MSFT_BackgroundTask[]

## 备注

## 相关链接

[Start-AppBackgroundTask](./Start-AppBackgroundTask.md)

[取消注册应用后台任务](./Unregister-AppBackgroundTask.md)

