---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/add-vmgroupmember?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-VMGroupMember
---

# 向虚拟机组（VMGroup）中添加成员

## 摘要
向虚拟机组中添加成员。

## 语法

### 使用名称的虚拟机（默认设置）
```
Add-VMGroupMember [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Name] <String> [-VM] <VirtualMachine[]> [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 使用名称的VMGroup
```
Add-VMGroupMember [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Name] <String> [-VMGroupMember] <VMGroup[]> [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 使用ID来识别虚拟机
```
Add-VMGroupMember [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Id] <Guid> [-VM] <VirtualMachine[]> [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 使用ID的VMGroup
```
Add-VMGroupMember [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Id] <Guid> [-VMGroupMember] <VMGroup[]> [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 使用 InputObject 的 VMGroup
```
Add-VMGroupMember [-VMGroup] <VMGroup> [-VMGroupMember] <VMGroup[]> [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 使用 InputObject 的虚拟机（VM）
```
Add-VMGroupMember [-VMGroup] <VMGroup> [-VM] <VirtualMachine[]> [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Add-VMGroupMember` cmdlet 用于将成员添加到虚拟机组中。一个虚拟机组可以包含单个虚拟机，也可以包含多个虚拟机组成的子组。

## 示例

### 示例 1：将虚拟机添加到组中
```
PS C:\> $VM01 = Get-VM -Name "ContosoVirtualMachine01"
PS C:\> $VM02 = Get-VM -Name "ContosoVirtualMachine02"
PS C:\> Add-VMGroupMember -Name "VirtualMachineGroup" -VM $VM01, $VM02
```

前两个命令使用了 **Get-VM** cmdlet 来获取名为 ContosoVirtualMachine01 和 ContosoVirtualMachine02 的虚拟机。这些命令将这些虚拟机对象存储在 `$VM01` 和 `$VM02` 变量中。

最后的命令将虚拟机 $VM01 和 $VM02 添加到名为 VirtualMachineGroup 的虚拟机组中。

### 示例 2：将一个组添加到另一个组中
```
PS C:\> $VMGroup01 = Get-VMGroup -Name "ContosoGroup01"
PS C:\> $VMGroup02 = Get-VMGroup -Name "ContosoGroup02"
PS C:\> Add-VMGroupMember -Name "ContosoMainGroup" -VMGroupMember $VMGroup01, $VMGroup02
```

前两个命令使用 **Get-VMGroup** cmdlet 来获取名为 ContosoGroup01 和 ContosoGroup02 的虚拟机组。这些命令将这些组对象存储在 `$VMGroup01` 和 `$VMGroup02` 变量中。

最后的命令将 `$VMGroup01` 和 `$VMGroup02` 中的组添加到名为 `ContosoMainGroup` 的组中。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: VM Using Name, VMGroup Using Name, VM Using ID, VMGroup Using ID
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个Hyper-V主机，在这些主机上此cmdlet会添加某个组成员。允许使用NetBIOS名称、IP地址或完全合格的域名作为目标主机标识。默认目标是本地计算机；可以使用“localhost”或点（.）来明确指代本地计算机。

```yaml
Type: String[]
Parameter Sets: VM Using Name, VMGroup Using Name, VM Using ID, VMGroup Using ID
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
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: VM Using Name, VMGroup Using Name, VM Using ID, VMGroup Using ID
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Id
指定该虚拟机组（此cmdlet用于向其中添加虚拟机或虚拟机组）的唯一ID。

```yaml
Type: Guid
Parameter Sets: VM Using ID, VMGroup Using ID
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定此cmdlet将虚拟机或虚拟机组添加到的虚拟机组的名称。

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
指定一个虚拟机数组，该cmdlet会将这些虚拟机添加到虚拟机组中。要获取一个**VirtualMachine**对象，请使用**Get-VM** cmdlet。

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
指定此cmdlet要向其添加虚拟机或虚拟机组的虚拟机组。若要获取一个**VMGroup**对象，请使用**Get-VMGroup** cmdlet。

```yaml
Type: VMGroup
Parameter Sets: VMGroup Using InputObject, VM Using InputObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMGroupMember
指定一个虚拟机组数组，该cmdlet会将这个数组添加到一个现有的虚拟机组中。

```yaml
Type: VMGroup[]
Parameter Sets: VMGroup Using Name, VMGroup Using ID, VMGroup Using InputObject
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
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
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMGroup
如果你指定了 `Passthru` 参数，此 cmdlet 会返回一个 `VMGroup` 对象。

## 备注

## 相关链接

[Remove-VMGroupMember](./Remove-VMGroupMember.md)

[Get-VM](./Get-VM.md)

[Get-VMGroup](./Get-VMGroup.md)

