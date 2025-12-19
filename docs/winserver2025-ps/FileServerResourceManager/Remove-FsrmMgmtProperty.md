---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FsrmMgmtProperty.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/remove-fsrmmgmtproperty?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-FsrmMgmtProperty
---

# 移除Fsrm管理属性

## 摘要
移除一个管理属性。

## 语法

```
Remove-FsrmMgmtProperty [-Namespace <String>] [-Name] <String> [-Recurse] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-FsrmMgmtProperty` cmdlet 用于从命名空间中删除某个管理属性。管理属性是一种分类属性，其 `AppliesTo` 属性中包含 “Folder”（文件夹），且其 `Flags` 属性不包含 “Secure” 这一标志。你可以使用 `Get-FsrmClassificationPropertyDefinition` cmdlet 来获取各种分类属性的定义。

## 示例

### 示例 1：删除所有管理属性
```
PS C:\> Remove-FsrmMgmtProperty -Name "FolderUsage_MS"
```

此命令会删除服务器上所有值为“FolderUsage_MS”的管理属性。

### 示例 2：使用命名空间来移除一个管理属性
```
PS C:\> Remove-FsrmMgmtProperty -Name "FolderUsage_MS" -Namespace "C:\Shares"
```

该命令会从命名空间 C:\Shares 中删除所有值为 “FolderUsage_MS” 的管理属性。

### 示例 3：删除命名空间层次结构中的所有管理属性
```
PS C:\> Remove-FsrmMgmtProperty -Name "FolderUsage_MS" -Namespace "C:\Shares" -Recurse
```

此命令会从命名空间“C:\ Shares”及其层次结构中所有下级命名空间中删除所有值为“FolderUsage_MS”的管理属性。

### 示例 4：删除命名空间层次结构中的所有管理属性
```
The first command gets all management properties on the server and stores the results in the $props variable.
PS C:\> $props = Get-FsrmMgmtProperty

The second command is a script that identifies management properties where the property applied on folders dos not exist anymore. The script uses the **Remove-FsrmMgmtProperty** cmdlet to remove the management properties for which there is no corresponding property definition on the server.
PS C:\> $nonExistingProperties = $props | where { $_.Exists -ne $true}
foreach ($candidate in $nonExistingProperties)
{foreach ($prop in $_.Properties) {Remove-FsrmMgmtProperty -Name $prop.Name -Namespace $candidate.Namespace}}
```

这个示例会从服务器上不存在的命名空间中删除所有管理属性。属性定义可以由管理员手动删除，或者由于组策略更新而被清除。当某个属性定义被删除后，服务器使用该属性定义为文件夹设置的相应管理属性值就变得无效（即不再具有任何意义）。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
在运行该 cmdlet 之前，会提示您进行确认。

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

### -Name
用于指定管理属性的名称。请在 **FsrmClassificationPropertyDefinition** 对象中设置该 “Name” 属性的值。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
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
该参数表示此cmdlet会删除命名空间中所有包含管理属性的文件夹的管理属性。如果您指定了此参数，还必须指定*Namespace*参数。

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
该参数用于指定可以同时运行的命令（cmdlet）的最大数量。如果省略此参数或输入值`0`，Windows PowerShell®将根据计算机上正在运行的CIM命令（cmdlets）的数量来计算该命令的最佳限制值。此限制仅适用于当前运行的命令，而不影响整个会话或计算机本身。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System.Management Automation.SwitchParameter

## 输出

### System.Object

## 备注

## 相关链接

[Get-FsrmClassificationPropertyDefinition](./Get-FsrmClassificationPropertyDefinition.md)

[Get-FsrmMgmtProperty](./Get-FsrmMgmtProperty.md)

[Set-FsrmMgmtProperty](./Set-FsrmMgmtProperty.md)

