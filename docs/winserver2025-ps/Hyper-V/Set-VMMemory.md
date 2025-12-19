---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/set-vmmemory?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-VMMemory
---

# Set-VMMemory

## 摘要
配置虚拟机的内存。

## 语法

### VMName（默认值）
```
Set-VMMemory [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String[]> [-Buffer <Int32>] [-DynamicMemoryEnabled <Boolean>] [-MaximumBytes <Int64>]
 [-StartupBytes <Int64>] [-MinimumBytes <Int64>] [-Priority <Int32>] [-MaximumAmountPerNumaNodeBytes <Int64>]
 [-ResourcePoolName <String>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject
```
Set-VMMemory [-VM] <VirtualMachine[]> [-Buffer <Int32>] [-DynamicMemoryEnabled <Boolean>]
 [-MaximumBytes <Int64>] [-StartupBytes <Int64>] [-MinimumBytes <Int64>] [-Priority <Int32>]
 [-MaximumAmountPerNumaNodeBytes <Int64>] [-ResourcePoolName <String>] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### ResourceObject
```
Set-VMMemory [-VMMemory] <VMMemory[]> [-Buffer <Int32>] [-DynamicMemoryEnabled <Boolean>]
 [-MaximumBytes <Int64>] [-StartupBytes <Int64>] [-MinimumBytes <Int64>] [-Priority <Int32>]
 [-MaximumAmountPerNumaNodeBytes <Int64>] [-ResourcePoolName <String>] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
**Set-VMMemory** cmdlet 用于配置虚拟机的内存。

## 示例

### 示例 1
```
PS C:\> Set-VMMemory TestVM -DynamicMemoryEnabled $true -MinimumBytes 64MB -StartupBytes 256MB -MaximumBytes 2GB -Priority 80 -Buffer 25
```

在虚拟机TestVM上启用动态内存功能，设置其最小内存、启动内存和最大内存容量、内存优先级以及缓冲区大小。

## 参数

### -Buffer
指定要在所配置的虚拟机中预留作为缓冲区的内存百分比。允许的值范围从5到2000。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于配置虚拟机内存的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行标识。默认值为本地计算机。可以使用 `localhost` 或点号（.`）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前会提示您确认是否要继续。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
默认值 value: False
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
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DynamicMemoryEnabled
指定是否要在要配置的虚拟机上启用动态内存功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaximumAmountPerNumaNodeBytes
指定要配置的虚拟机中每个 NUMA 节点的最大内存使用量。

```yaml
Type: Int64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaximumBytes
指定启用了动态内存的虚拟机可以使用的最大内存容量。

```yaml
Type: Int64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MinimumBytes
指定已启用动态内存的虚拟机所需使用的最小内存容量。

```yaml
Type: Int64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定需要将一个 **Microsoft.HyperV POWERShell.Memory** 对象传递给管道，该对象代表要配置的虚拟机内存。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Priority
设置该虚拟机在内存可用性方面的优先级，相对于同一虚拟机主机上的其他虚拟机而言。允许的值范围是 0 到 100。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResourcePoolName
指定此虚拟机的内存资源池的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -StartupBytes
指定为启用了动态内存的虚拟机分配的初始内存量，或者为未启用动态内存的虚拟机分配的总内存量。

```yaml
Type: Int64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定要配置内存的虚拟机。

```yaml
Type: VirtualMachine[]
Parameter Sets: VMObject
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMMemory
指定要配置的虚拟机内存。

```yaml
Type: VMMemory[]
Parameter Sets: ResourceObject
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定要配置内存的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
默认值 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值

### Microsoft.HyperV.PowerShell MEMORY
如果指定了**-PassThru**选项。

## 备注

## 相关链接

