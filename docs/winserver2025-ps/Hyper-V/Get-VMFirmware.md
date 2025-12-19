---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmfirmware?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMFirmware
---

# 获取虚拟机固件信息（Get-VMFirmware）

## 摘要
获取虚拟机的固件配置信息。

## 语法

### VMName（默认值）
```
Get-VMFirmware [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String[]> [<CommonParameters>]
```

### VMObject
```
Get-VMFirmware [-VM] <VirtualMachine[]> [<CommonParameters>]
```

### VMSnapshot
```
Get-VMFirmware [-VMSnapshot] <VMSnapshot> [<CommonParameters>]
```

## 描述
`Get-VMFirmware` cmdlet 可用于获取虚拟机的固件配置信息。注意：此 cmdlet 仅支持第 2 代虚拟机。

## 示例

### 示例 1
```
PS C:\> Get-VMFirmware "Test VM"
```

这个示例为名为“Test VM”的虚拟机返回一个虚拟机固件对象。

## 参数

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。请输入计算机名称或会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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
指定一个包含 Hyper-V 主机的数组。此 cmdlet 会从您指定的主机中获取虚拟机的固件信息。

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
用于指定一个虚拟机对象数组。该cmdlet会获取您所指定的虚拟机的固件配置信息。若需获取某个虚拟机对象，请使用**Get-VM** cmdlet。

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
指定一个虚拟机名称数组。此 cmdlet 会获取所指定虚拟机的固件配置信息。

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
指定在检索固件配置时将与虚拟机（VM）一起使用的虚拟机快照。

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
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMFirmware

## 备注
* Note: This cmdlet is supported only on Generation 2 virtual machines.

## 相关链接

[Set-VMFirmware](./Set-VMFirmware.md)

