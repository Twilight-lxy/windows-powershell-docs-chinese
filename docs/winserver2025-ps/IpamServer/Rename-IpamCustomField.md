---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamCustomField.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/rename-ipamcustomfield?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Rename-IpamCustomField
---

# 重命名 Ipam 自定义字段

## 摘要
在 IPAM 中重命名一个自定义字段。

## 语法

```
Rename-IpamCustomField [-Name] <String> [-newName] <String> [-PassThru] [-Force] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Rename-IpamCustomField` 这个 cmdlet 用于重命名 Internet 协议地址管理（IPAM）中用户自定义的字段。该 cmdlet 仅更改自定义字段的名称，而与其他自定义字段的关联以及对该字段在其他 IPAM 对象中的赋值关系仍然有效。您无法重命名 IPAM 中内置的自定义字段。

## 示例

### 示例 1：重命名用户自定义的字段
```
PS C:\> Rename-IpamCustomField -Name "Building" -newName "Building_Main" -PassThru
Name                          Category                      MultiValue                    CustomValue

----                          --------                      ----------                    -----------

Building_Main              UserDefined                   True                          {B1, B2, B3}
```

这个命令将用户自定义的自定义字段“Building”重命名为“Building_Main”。

该命令包含了*PassThru*参数，因此会将结果显示在控制台上。

## 参数

### -AsJob
将此 cmdlet 作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，随后会显示命令提示符。在作业完成之前，您可以继续在当前会话中操作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，则可以使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

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

### -Force
强制命令运行，而无需请求用户确认。

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

### -Name
指定一个自定义字段的名称。

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

### -PassThru
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -ThrottleLimit
该参数用于指定可以同时运行的命令（cmdlet）的最大数量。如果省略此参数或输入值为`0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令（cmdlets）的数量来计算一个最优的并发限制。这个并发限制仅适用于当前正在运行的命令，而不适用于整个会话或整个计算机。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并未运行该cmdlet。

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

### -newName
为自定义字段指定一个新的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### IpamCustomField
这个cmdlet返回一个对象，该对象代表IPAM服务器中的一个自定义元数据字段。

## 备注

## 相关链接

[Get-IpamCustomField](./Get-IpamCustomField.md)

[Add-IpamCustomField](./Add-IpamCustomField.md)

[Remove-IpamCustomField](./Remove-IpamCustomField.md)

