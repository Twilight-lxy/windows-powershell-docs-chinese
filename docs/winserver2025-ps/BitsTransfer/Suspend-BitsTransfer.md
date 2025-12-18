---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.BackgroundIntelligentTransfer.Management.dll-Help.xml
Module Name: BitsTransfer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/bitstransfer/suspend-bitstransfer?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Suspend-BitsTransfer
---

# 暂停比特传输

## 摘要
暂停一个BITS传输作业。

## 语法

```
Suspend-BitsTransfer [-BitsJob] <BitsJob[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Suspend-BitsTransfer` cmdlet 可以暂停一个或多个后台智能传输服务（Background Intelligent Transfer Service，简称 BITS）的传输任务。如果传输任务已经处于暂停状态，该 cmdlet 将不会产生任何效果。您可以使用 `Resume-BitsTransfer` cmdlet 来重新启动 BITS 传输任务。

## 示例

### 示例 1：暂停当前用户拥有的所有 BITS（Binary Transfer Service）传输作业
```
PS C:\> Get-BitsTransfer | Suspend-BitsTransfer
```

此命令会暂停当前用户拥有的所有BITS传输作业。

`Get-BitsTransfer` 的输出是一组 `BitsJob` 对象。这些输出会被传递给 `Suspend-BitsTransfer` cmdlet。

### 示例 2：暂停计算机上所有的 BITS（Binary Transfer Service）传输任务
```
PS C:\> $Bits = Get-BitsTransfer -AllUsers
PS C:\> Suspend-BitsTransfer -BitsJob $Bits
```

这个命令会暂停计算机上所有的BITS传输作业。

第一个命令获取计算机上所有的 **BitsJob** 对象，然后将它们存储在 `$Bits` 变量中。

第二个命令使用 *BitsJob* 参数，将存储在 $Bits 变量中的 **BitsJob** 对象传递给 **Suspend-BitsTransfer** cmdlet。

## 参数

### -BitsJob
用于指定需要暂停的 BITS（Bit Transfer Service）传输任务。您可以从其他返回 **BitsJob** 对象的 cmdlet（例如 **Get-BitsTransfer**）中将该对象的值传递给此参数。

```yaml
Type: BitsJob[]
Parameter Sets: (All)
Aliases: b

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
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

### -WhatIf
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

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

### Microsoft BackgroundIntelligentTransferManagement.BitsJob[]
此cmdlet接受一个或多个**BitsJob**对象作为输入，并将这些对象填充到*BitsJob*参数中。

## 输出

### Microsoft BackgroundIntelligentTransferManagement.BitsJob[]
此cmdlet会生成与那些被挂起的BITS传输任务相关的**BitsJob**对象。

## 备注

## 相关链接

[Add-BitsFile](./Add-BitsFile.md)

[Complete-BitsTransfer](./Complete-BitsTransfer.md)

[Get-BitsTransfer](./Get-BitsTransfer.md)

[Remove-BitsTransfer](./Remove-BitsTransfer.md)

[Resume-BitsTransfer](./Resume-BitsTransfer.md)

[Set-BitsTransfer](./Set-BitsTransfer.md)

[开始比特传输](./Start-BitsTransfer.md)

