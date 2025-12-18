---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.BackgroundIntelligentTransfer.Management.dll-Help.xml
Module Name: BitsTransfer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/bitstransfer/remove-bitstransfer?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-BitsTransfer
---

# Remove-BitsTransfer

## 摘要
取消一个BITS传输任务。

## 语法

```
Remove-BitsTransfer [-BitsJob] <BitsJob[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-BitsTransfer` cmdlet 用于取消后台智能传输服务（Background Intelligent Transfer Service，简称 BITS）的传输作业。它会删除相关的传输任务、客户端上的所有临时文件，并移除相应的 `BitsJob` 对象。

当 `Remove-BitsTransfer` cmdlet 取消一个传输作业时，它会删除所有相关的传输任务。假设你正在传输三个文件：其中一个文件已经完全传输完成，另一个文件正处于传输过程中，还有一个文件仍在传输中。在这种情况下，`Remove-BitsTransfer` 会取消整个传输操作，并删除相关文件。使用 `Remove-BitsTransfer` cmdlet 取消传输作业后，之前已传输完成的文件将无法再次访问。如果你需要的话，可以使用 `Complete-BitsTransfer` cmdlet 来完成那些已经成功下载的文件的传输过程，并取消尚未完成或正在进行的传输任务。在这种情况下，已传输完成的文件不会被删除，仍然可以正常使用。

## 示例

### 示例 1：取消当前用户拥有的所有 BITS（Binary Transfer System）传输作业
```
PS C:\> Get-BitsTransfer | Remove-BitsTransfer
```

这个命令会取消当前用户所拥有的所有BITS传输作业。

`Get-BitsTransfer` cmdlet 的输出结果被传递给 `Remove-BitsTransfer` cmdlet。该输出结果是一组 `BitsJob` 对象。

### 示例 2：取消计算机上所有 BITS 数据传输任务
```
C:\PS>$Bits = Get-BitsTransfer -AllUsers
PS C:\> Remove-BitsTransfer -BitsJob $Bits
```

这个命令会取消计算机上所有与BITS（BitTorrent Transfer Service）相关的传输任务。

第一个命令会获取计算机上所有的 **BitsJob** 对象，并将它们存储在 `$Bits` 变量中。

第二个命令使用了 *BitsJob* 参数，将存储在 $Bits 变量中的 **BitsJob** 对象传递给 **Remove-BitsTransfer** cmdlet。

## 参数

### -BitsJob
用于指定需要取消的 BITS 传输作业数组。您可以从返回 **BitsJob** 对象的其他 cmdlet（例如 **Get-BitsTransfer** cmdlet）中将相关值传递给此参数。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.BackgroundIntelligentTransfer.Management.BitsJob[]
此cmdlet接受一个或多个**BitsJob**对象作为输入，并将这些对象赋值给*BitsJob*参数。

## 输出

### 无
这个cmdlet不会生成任何输出。

## 备注
* After a job is removed or completed, any job objects that were previously cached in variables or in scripts are no longer valid.

## 相关链接

[Add-BitsFile](./Add-BitsFile.md)

[完成位传输](./Complete-BitsTransfer.md)

[Get-BitsTransfer](./Get-BitsTransfer.md)

[Resume-BitsTransfer](./Resume-BitsTransfer.md)

[Set-BitsTransfer](./Set-BitsTransfer.md)

[开始比特传输](./Start-BitsTransfer.md)

[Suspend-BitsTransfer](./Suspend-BitsTransfer.md)

