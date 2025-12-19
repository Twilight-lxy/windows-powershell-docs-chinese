---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/remove-vmgroupmember?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-VMGroupMember
---

# 移除VM组成员

## 摘要
从虚拟机组中删除成员。

## 语法

### 使用名称的虚拟机（默认设置）
```
Remove-VMGroupMember [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Name] <String> [-VM] <VirtualMachine[]> [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 使用ID的VMGroup
```
Remove-VMGroupMember [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Id] <Guid> [-VMGroupMember] <VMGroup[]> [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 使用名称来引用VMGroup
```
Remove-VMGroupMember [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Name] <String> [-VMGroupMember] <VMGroup[]> [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 使用ID来识别虚拟机
```
Remove-VMGroupMember [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Id] <Guid> [-VM] <VirtualMachine[]> [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 使用 InputObject 的虚拟机（VM）
```
Remove-VMGroupMember [-VMGroup] <VMGroup> [-VM] <VirtualMachine[]> [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 使用 InputObject 的 VMGroup
```
Remove-VMGroupMember [-VMGroup] <VMGroup> [-VMGroupMember] <VMGroup[]> [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Remove-VMGroupMember` cmdlet 可以将单个虚拟机或一组虚拟机从虚拟机组中移除。

## 示例

### 示例 1：从组中移除虚拟机
```
PS C:\> $VM01 = Get-VM -Name "ContosoVirtualMachine01"
PS C:\> Remove-VMGroupMember -Name "VirtualMachineGroup" -VM $VM01
```

第一个命令使用了 **Get-VM** cmdlet 来获取一个名为 ContosoVirtualMachine01 的虚拟机。该命令将这个虚拟机对象存储在 **$VM01** 变量中。

第二个命令会将名为 **$VM01** 的虚拟机从名为 VirtualMachineGroup 的组中移除。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: VM Using Name, VMGroup Using ID, VMGroup Using Name, VM Using ID
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个运行此 cmdlet 的 Hyper-V 主机。允许使用 NetBIOS 名称、IP 地址和完全限定域名进行标识。默认值为本地计算机。可以使用 `localhost` 或点（.`）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VM Using Name, VMGroup Using ID, VMGroup Using Name, VM Using ID
Aliases:

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

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值是当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: VM Using Name, VMGroup Using ID, VMGroup Using Name, VM Using ID
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Id
指定该虚拟机组（从这个虚拟机组中移除虚拟机或虚拟机组）的唯一标识符。

```yaml
Type: Guid
Parameter Sets: VMGroup Using ID, VM Using ID
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定此 cmdlet 从中删除虚拟机或虚拟机组的虚拟机组的名称。

```yaml
Type: String
Parameter Sets: VM Using Name, VMGroup Using Name
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
表示此 cmdlet 会返回其配置的 **Microsoft.HyperV.PowerShell.VMGroup** 对象。

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
指定一个虚拟机数组，该cmdlet将从这个虚拟机组中删除这些虚拟机。要获取一个**VirtualMachine**对象，请使用**Get-VM** cmdlet。

```yaml
Type: VirtualMachine[]
Parameter Sets: VM Using Name, VM Using ID, VM Using InputObject
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMGroup
指定此 cmdlet 从其中删除虚拟机或虚拟机组所在的虚拟机组。若要获取一个 **VMGroup** 对象，请使用 **Get-VMGroup** cmdlet。

```yaml
Type: VMGroup
Parameter Sets: VM Using InputObject, VMGroup Using InputObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMGroupMember
指定一个虚拟机组数组，该cmdlet将从这个虚拟机组中删除这些虚拟机组。

```yaml
Type: VMGroup[]
Parameter Sets: VMGroup Using ID, VMGroup Using Name, VMGroup Using InputObject
Aliases:

Required: True
Position: 1
Default value: None
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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMGroup
如果你指定了 **Passthruf** 参数，此 cmdlet 会返回一个 **VMGroup** 对象。

## 备注

## 相关链接

[Add-VMGroupMember](./Add-VMGroupMember.md)

[Get-VM](./Get-VM.md)

[Get-VMGroup](./Get-VMGroup.md)

