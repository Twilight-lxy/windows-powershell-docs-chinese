---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/rename-vmnetworkadapter?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Rename-VMNetworkAdapter
---

# 重命名虚拟机网络适配器

## 摘要
重命名虚拟机或管理操作系统上的虚拟网络适配器。

## 语法

### VMName（默认值）
```
Rename-VMNetworkAdapter [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String[]> [[-Name] <String>] [-NewName] <String> [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### ResourceObject
```
Rename-VMNetworkAdapter [-VMNetworkAdapter] <VMNetworkAdapterBase[]> [-NewName] <String> [-Passthru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### ManagementOS
```
Rename-VMNetworkAdapter [-ManagementOS] [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [[-Name] <String>] [-NewName] <String> [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### VMObject
```
Rename-VMNetworkAdapter [-VM] <VirtualMachine[]> [[-Name] <String>] [-NewName] <String> [-Passthru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Rename-VMNetworkAdapter` cmdlet 可以重命名虚拟机或管理操作系统上的虚拟网络适配器。

## 示例

### 示例 1
```
PS C:\> Rename-VMNetworkAdapter -VMName Redmond -NewName CoreNet
```

这个示例将虚拟机Redmond的所有虚拟网络适配器的名称更改为CoreNet。

### 示例 2
```
PS C:\> Rename-VMNetworkAdapter -VMName Kirkland -Name Private -NewName CoreNet
```

这个示例将虚拟机“Kirkland”中的虚拟网络适配器的名称从“Private”更改为“CoreNet”。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，使用的是本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: VMName, ManagementOS
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于重命名虚拟网络适配器的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行识别。默认值是本地计算机；可以通过使用 `localhost` 或点号（.`）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName, ManagementOS
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前，会提示您进行确认。

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

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: VMName, ManagementOS
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ManagementOS
指定您想要重命名属于管理操作系统的虚拟网络适配器。

```yaml
Type: SwitchParameter
Parameter Sets: ManagementOS
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定虚拟网络适配器的现有名称。

```yaml
Type: String
Parameter Sets: VMName, ManagementOS, VMObject
Aliases: VMNetworkAdapterName

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NewName
指定虚拟网络适配器的新名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定要将某个对象传递给代表需要重命名的虚拟网络适配器的管道。如果指定了 `ManagementOS`，则该对象为 `Microsoft.HyperV POWERShell.VMInternalNetworkAdapter` 类型；否则，该对象为 `Microsoft.HyperV.PowerShell.VMNetworkAdapter` 类型。

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

### -VM
指定包含您想要重命名的虚拟网络适配器的虚拟机。

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
指定拥有您希望重命名的虚拟网络适配器的虚拟机的名称。

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

### -VMNetworkAdapter
指定要重命名的虚拟网络适配器。

```yaml
Type: VMNetworkAdapterBase[]
Parameter Sets: ResourceObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无

默认情况下，此cmdlet不会返回任何输出结果。

### Microsoft.HyperV.PowerShell.VMNetworkAdapter

当你使用 **PassThru** 参数时，此 cmdlet 会返回一个 **Microsoft.HyperV POWERShell.VMNetworkAdapter** 对象。

### Microsoft.HyperV.PowerShell.VMInternalNetworkAdapter

当您使用 **PassThru** 和 **-ManagementOS** 参数时，此 cmdlet 会返回一个 **Microsoft.HyperV.PowShell.VMInternalNetworkAdapter** 对象。

## 备注

## 相关链接

