---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/remove-vmscsicontroller?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-VMScsiController
---

# 移除 VMScsiController

## 摘要
从虚拟机中移除一个SCSI控制器。

## 语法

### VMName（默认值）
```
Remove-VMScsiController [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String[]> [-ControllerNumber] <Int32> [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 对象
```
Remove-VMScsiController [-VMScsiController] <VMScsiController[]> [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Remove-VMScsiController` cmdlet 用于从虚拟机中删除 SCSI 控制器。

## 示例

### 示例 1
```
PS C:\> Get-VMScsiController -VMName TestVM -ControllerNumber 0 | Remove-VMScsiController
```

从虚拟机TestVM中删除SCSI控制器0。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个要从其中卸载 SCSI 控制器的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全 Qualified 域名进行指定。默认值为本地计算机。可以使用 `localhost` 或点号（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行 cmdlet 之前会提示您进行确认。

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

### -ControllerNumber
指定控制器的编号。该cmdlet会删除您所指定的SCSI控制器。

```yaml
Type: Int32
Parameter Sets: VMName
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定需要将一个 **VMScsiController** 对象传递给流水线，该对象代表要移除的 SCSI 控制器。

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

### -VMName
指定一个虚拟机名称数组。该cmdlet会从您指定的虚拟机上删除SCSI控制器。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMScsiController
指定要删除的 SCSI 控制器。

```yaml
Type: VMScsiController[]
Parameter Sets: Object
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
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

## 输出

### 无

默认情况下，此cmdlet不会返回任何输出结果。

### VMScsiController

当你使用 **PassThru** 参数时，此 cmdlet 会返回一个 **VMScsiController** 对象。

## 备注

## 相关链接
