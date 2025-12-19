---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FsrmAdrSetting.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/get-fsrmadrsetting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-FsrmAdrSetting
---

# Get-FsrmAdrSetting

## 摘要
获取与事件相关的“访问被拒绝”问题的修复设置信息。

## 语法

```
Get-FsrmAdrSetting [[-Event] <FsrmAdrEventEnum[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [<CommonParameters>]
```

## 描述
`Get-FsrmAdrSetting` cmdlet 可用于获取文件服务器资源管理器（FSRM）中针对一个或多个事件的访问拒绝修复（Access Denied Remediation, ADR）设置。

当客户端无法访问某个文件时，Windows Server 2016会使用“自动离线恢复”（ADR）设置。如果用户试图访问他们没有权限的文件服务器上的共享文件和文件夹，他们会收到“访问被拒绝”的提示信息。

## 示例

### 示例 1：获取 FSRM 访问被拒绝的设置
```
PS C:\> Get-FsrmAdrSetting -Event AccessDenied
```

这个命令可以获取FSRM中所有关于“访问被拒绝”的设置信息。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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

### -Event
指定 ADR 处理的事件类型数组。此参数的可接受值为：AccessDenied 和 FileNotFound。

```yaml
Type: FsrmAdrEventEnum[]
Parameter Sets: (All)
Aliases:
Accepted values: AccessDenied, FileNotFound

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算出一个最优的节流限制。这个节流限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.PowerShell Cmdletization GeneratedTypes.FsrmAdrEventEnum[]

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

### Microsoft.ManagementInfrastructure.CimInstance#Root/Microsoft/Windows/FSRM/MSFT_FSRMADRSettings

## 备注

## 相关链接

[Set-FsrmAdrSetting](./Set-FsrmAdrSetting.md)

