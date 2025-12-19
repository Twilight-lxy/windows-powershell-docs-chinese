---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/disable-vmresourcemetering?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-VMResourceMetering
---

# 禁用虚拟机资源计量功能

## 摘要
停止收集虚拟机的资源使用情况数据。

## 语法

### VMName（默认值）
```
Disable-VMResourceMetering [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-VMName] <String[]> [<CommonParameters>]
```

### ResourcePool
```
Disable-VMResourceMetering [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-ResourcePoolName] <String> [[-ResourcePoolType] <VMResourcePoolType>]
 [<CommonParameters>]
```

### VMObject
```
Disable-VMResourceMetering [-VM] <VirtualMachine[]> [<CommonParameters>]
```

## 描述
**Disable-VMResourceMetering** 这个 cmdlet 用于禁用对虚拟机或资源池的资源使用情况数据的收集。

调用此cmdlet会停止数据收集，并删除截至调用时的所有已收集的数据。

通话结束后，Measure-VM 和 Measure-VMResourcePool 将无法使用。

## 示例

### 示例 1
```
PS C:\> Disable-VMResourceMetering -VMName TestVM
```

禁用对名为TestVM的虚拟机收集资源利用数据的功能。

### 示例 2
```
PS C:\> Get-VM Test* | Disable-VMResourceMetering
```

禁用对名称以“Test”开头的虚拟机集合的资源利用数据的收集功能。

### 示例 3
```
PS C:\> Disable-VMResourceMetering -ResourcePoolName TestResourcePool -ResourcePoolType Memory
```

禁用对名为“TestResourcePool”的内存类型资源池的资源利用数据的收集功能。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。您可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: VMName, ResourcePool
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个Hyper-V主机，在这些主机上将禁用资源利用率数据的收集。可以使用NetBIOS名称、IP地址或完全限定域名进行指定。默认值为本地计算机。可以使用“localhost”或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName, ResourcePool
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
Parameter Sets: VMName, ResourcePool
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResourcePoolName
指定资源池的友好名称，该资源池上的资源使用数据收集功能将被禁用。

```yaml
Type: String
Parameter Sets: ResourcePool
Aliases: Name

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -ResourcePoolType
指定要禁用资源利用率数据收集的资源池的资源类型。

```yaml
Type: VMResourcePoolType
Parameter Sets: ResourcePool
Aliases:
Accepted values: Ethernet, Memory, Processor, VHD

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -VM
指定要禁用资源利用率数据收集的虚拟机。

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
指定要禁用资源利用率数据收集的虚拟机的友好名称。

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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.HyperV POWERShell VirtualMachine[]

### Microsoft.HyperV.PowerShell.VMResourcePoolType

## 输出

## 备注

## 相关链接

[Measure-VM](./Measure-VM.md)

[Measure-VMResourcePool](./Measure-VMResourcePool.md)

[Enable-VMResourceMetering](./Enable-VMResourceMetering.md)

