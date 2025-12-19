---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FsrmMgmtProperty.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/get-fsrmmgmtproperty?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-FsrmMgmtProperty
---

# Get-FsrmMgmtProperty

## 摘要
获取管理属性。

## 语法

```
Get-FsrmMgmtProperty [-Namespace <String>] [-Name <String>] [-Recurse] [-Effective]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Get-FsrmMgmtProperty` cmdlet 用于获取文件服务器资源管理器（FSRM）中某个命名空间的管理属性。管理属性是一种分类属性，其 `AppliesTo` 属性中包含 “Folder”（文件夹），并且其 `Flags` 属性不包含 “Secure” （安全）值。你可以使用 `Get-FsrmClassificationPropertyDefinition` cmdlet 来获取这些分类属性的定义。

## 示例

### 示例 1：获取所有管理属性
```
PS C:\> Get-FsrmMgmtProperty
```

这个命令可以获取服务器的所有管理属性。

### 示例 2：使用命名空间获取管理属性
```
PS C:\> Get-FsrmMgmtProperty -Namespace "C:\Shares"
```

这个命令用于获取文件夹 C:\Shares 的“文件夹使用情况”（Folder Usage）属性。

### 示例 3：通过名称获取管理属性
```
PS C:\> Get-FsrmMgmtProperty -Namespace "C:\Shares" -Name "FolderUsage_MS"
```

此命令用于获取文件夹 C:\Shares 中名为 FolderUsage_MS 的管理属性对应的“文件夹使用情况”（Folder Usage）信息。

### 示例 4：获取路径中所有文件夹的管理属性
```
PS C:\> Get-FsrmMgmtProperty -Namespace "C:\Shares" -Recurse
```

此命令会获取 C:\Shares 及该路径下所有文件夹的管理属性。

### 示例 5：通过名称获取最近的管理属性
```
PS C:\> Get-FsrmMgmtProperty -Namespace "C:\Shares\CtrShares03" -Name "FolderUsage_MS" -Effective
```

这个命令用于获取 C:\Shares\CtrShares03 文件夹的 `FolderUsage` 属性值。如果在 C:\Shares\CtrShares03 中没有名为 `FolderUsage_MS` 的文件夹使用管理属性，那么该 cmdlet 会搜索整个命名空间（C:\shares、C:\\），并找到第一个与该管理属性相关的条目。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行需要较长时间才能完成的命令。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

### -Confirm
在运行 cmdlet 之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Effective
该cmdlet用于获取名称与您所指定的值相匹配的最近文件夹的管理属性。cmdlet会根据您指定的命名空间或父级层次结构来查找相应的管理属性。如果您指定了此参数，则必须同时指定*Name*参数。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
用于指定某个管理属性的名称。请在 **FsrmClassificationPropertyDefinition** 对象中设置该属性的值。如果您不指定此参数，该 cmdlet 将获取服务器上的所有管理属性。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Namespace
指定一个文件夹的本地路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Recurse
该参数表示此cmdlet会获取命名空间中所有包含管理属性的文件夹的管理属性。如果您指定了此参数，就必须同时指定*Namespace*参数。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算相应的最佳限制值。该限制仅适用于当前执行的 cmdlet，而不影响整个会话或计算机本身的运行状态。

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System.Management.Automation.SwitchParameter

## 输出

### Microsoft.ManagementInfrastructure.CimInstance[]

## 备注

## 相关链接

[Get-FsrmClassificationPropertyDefinition](./Get-FsrmClassificationPropertyDefinition.md)

[Remove-FsrmMgmtProperty](./Remove-FsrmMgmtProperty.md)

[Set-FsrmMgmtProperty](./Set-FsrmMgmtProperty.md)

