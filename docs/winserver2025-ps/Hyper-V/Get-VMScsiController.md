---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmscsicontroller?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMScsiController
---

# Get-VMScsiController

## 摘要
获取虚拟机或快照的SCSI控制器信息。

## 语法

### VMName（默认值）
```
Get-VMScsiController [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String[]> [[-ControllerNumber] <Int32>] [<CommonParameters>]
```

### VMSnapshot
```
Get-VMScsiController [-VMSnapshot] <VMSnapshot> [[-ControllerNumber] <Int32>] [<CommonParameters>]
```

### VMObject
```
Get-VMScsiController [[-ControllerNumber] <Int32>] [-VM] <VirtualMachine[]> [<CommonParameters>]
```

## 描述
`Get-VMScsiController` cmdlet 可以获取虚拟机或快照的 SCSI 控制器信息。

## 示例

### 示例 1
```
PS C:\> Get-VMScsiController -VMName TestVM -ControllerNumber 0
```

从虚拟机TestVM获取SCSI控制器0。

### 示例 2
```
PS C:\> Get-VM -Name TestVM -ComputerName Development | Get-VMScsiController
```

从位于Hyper-V主机Development上的虚拟机TestVM中获取SCSI控制器。

### 示例 3
```
PS C:\> Get-VMSnapshot -VMName TestVM -Name 'Before applying updates' | Get-VMScsiController
```

在应用虚拟机TestVM的更新之前，从快照中获取SCSI控制器信息。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
指定一个或多个用于检索 SCSI 控制器的 Hyper-V 主机。允许使用 NetBIOS 名称、IP 地址或完全限定域名。默认值为本地计算机。可以使用 “localhost” 或点（.）来明确表示本地计算机。

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

### -ControllerNumber
指定要获取的SCSI控制器的编号。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
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

### -VM
指定要获取其SCSI控制器的虚拟机。

```yaml
Type: VirtualMachine[]
Parameter Sets: VMObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定要获取其SCSI控制器信息的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMSnapshot
指定要检索其SCSI控制器的快照。

```yaml
Type: VMSnapshot
Parameter Sets: VMSnapshot
Aliases: VMCheckpoint

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMScsiController

## 备注

## 相关链接

