---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ps_mmagent_v1.0.cdxml-help.xml
Module Name: MMAgent
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/mmagent/debug-mmappprelaunch?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Debug-MMAppPrelaunch
---

# 调试 MMApp 的预启动过程

## 摘要
在特定应用程序启动之前，通过触发其预启动过程来调试该应用程序，并使该应用程序退出调试模式。

## 语法

```
Debug-MMAppPrelaunch -PackageFullName <String> [-DisableDebugMode] -PackageRelativeAppId <String>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Debug-MMAppPrelaunch` cmdlet 用于在特定应用程序启动前对其进行调试。它会触发该应用程序的预启动过程，并使应用程序退出调试模式。

“预启动”（Prelaunching）是Windows® 8.1中新增的一项功能，它通过在后台主动启动那些经常使用的应用程序（如果这些程序尚未运行或处于挂起状态的话），来提升从Windows应用商店启动应用程序的速度。从用户的角度来看，使用这项功能启动一个应用程序的速度几乎与切换到一个已挂起的程序一样快。该命令允许你将某个应用程序预先设置为调试模式（Debug mode）进行启动。

您可以通过包含 *PackageFullName* 和 *PackageRelativeAppId* 参数来指定要预启动的应用程序。

要关闭调试功能，请指定应用程序，并添加 * DisableDebugMode* 参数。

## 示例

#### 示例 1：预启动应用程序并启用调试模式
```
PS C:\> Debug-MmAppPreLaunch -PackageFullName Microsoft.ZuneMusic_2.0.94.0_x64__8wekyb3d8bbwe -PackageRelativeAppId Microsoft.ZuneMusic
```

此命令以调试模式预先启动一个应用程序。

### 示例 2：从预启动状态下激活的应用程序中清除调试模式
```
PS C:\> Debug-MmAppPreLaunch -PackageFullName Microsoft.ZuneMusic_2.0.94.0_x64__8wekyb3d8bbwe -PackageRelativeAppId Microsoft.ZuneMusic -DisableDebugMode
```

此命令将禁用您之前预先启动并激活的应用程序中的调试模式。

#### 示例 3：获取您应用程序的 `PackageFullName` 和 `PackageRelativeAppId`
```
PS C:\> ForEach ($Package in Get-AppxPackage) {ForEach ($AppRelativeId in (Get-AppxPackageManifest($Package)).Package.Applications.Application.Id) {'PackageFullName: ' + $Package.PackageFullName; 'PackageRelativeId: ' + $AppRelativeID; ''}}
```

这个命令展示了如何获取你的包对应的 `PackageFullName` 和 `PackageRelativeAppId` 信息。

## 参数

### -AsJob
将 cmdlet 作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个代表该作业的对象，随后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -DisableDebugMode
表示该cmdlet会关闭所选应用程序的调试模式。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: ddm

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PackageFullName
指定包含应用程序的AppX包的完整名称，该应用程序将以调试模式进行预启动。

```yaml
Type: String
Parameter Sets: (All)
Aliases: pfn

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PackageRelativeAppId
指定在 AppX 包中预先启动的应用程序的应用程序 ID。该应用程序 ID 可以在包清单文件中找到。

```yaml
Type: String
Parameter Sets: (All)
Aliases: praid

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的并发操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

## 备注
* None

## 相关链接

[ Disable-MMAgent](./Disable-MMAgent.md)

[Enable-MMAgent](./Enable-MMAgent.md)

[Get-MMAgent](./Get-MMAgent.md)

[Set-MMAgent](./Set-MMAgent.md)

