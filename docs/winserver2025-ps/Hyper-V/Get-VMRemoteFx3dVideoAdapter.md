---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmremotefx3dvideoadapter?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMRemoteFx3dVideoAdapter
---

# 获取-VMRemoteFx3dVideoAdapter

## 摘要
获取虚拟机或快照的RemoteFX视频适配器信息。

## 语法

### VMName（默认值）
```
Get-VMRemoteFx3dVideoAdapter [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-VMName] <String[]> [<CommonParameters>]
```

### VMObject
```
Get-VMRemoteFx3dVideoAdapter [-VM] <VirtualMachine[]> [<CommonParameters>]
```

### VMSnapshot
```
Get-VMRemoteFx3dVideoAdapter [-VMSnapshot] <VMSnapshot> [<CommonParameters>]
```

## 描述
`Get-VMRemoteFx3dVideoAdapter` cmdlet 可用于获取虚拟机或快照的 RemoteFX 视频适配器。

## 示例

### 示例 1
```
PS C:\> Get-VMRemoteFx3dVideoAdapter -VMName TestVM
```

从虚拟机 TestVM 中获取 RemoteFX 适配器。

### 示例 2
```
PS C:\> Get-VM -Name TestVM | Get-VMRemoteFx3dVideoAdapter
```

从虚拟机TestVM中获取RemoteFx适配器。

### 示例 3
```
PS C:\> Get-VMSnapshot -VMName TestVM -Name 'Before applying updates' | Get-VMRemoteFx3dVideoAdapter
```

在应用虚拟机TestVM的更新之前，从快照中获取RemoteFx适配器。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
指定一个或多个用于获取 RemoteFX 视频适配器的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全 Qualified Domain Name（FQDN）来进行选择。默认值是本地计算机。可以通过使用 `localhost` 或点号（.）来明确表示本地计算机。

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
指定要获取其RemoteFX视频适配器的虚拟机。

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
指定要获取其RemoteFX视频适配器的虚拟机的名称。

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
指定要获取其RemoteFX视频适配器信息的快照。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMRemoteFx3DVideoAdapter

## 备注

## 相关链接

