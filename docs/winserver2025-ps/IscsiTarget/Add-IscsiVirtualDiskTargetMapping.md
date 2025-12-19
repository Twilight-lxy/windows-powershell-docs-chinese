---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Iscsi.Target.Commands.dll-Help.xml
Module Name: IscsiTarget
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsitarget/add-iscsivirtualdisktargetmapping?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-IscsiVirtualDiskTargetMapping
---

# Add-IscsiVirtualDiskTargetMapping

## 摘要
将一个虚拟磁盘分配给一个iSCSI目标设备。

## 语法

```
Add-IscsiVirtualDiskTargetMapping [-TargetName] <String> [-Path] <String> [-Lun <Int32>]
 [-ComputerName <String>] [-Credential <PSCredential>] [<CommonParameters>]
```

## 描述
**Add-IscsiVirtualDiskTargetMapping** cmdlet 将一个虚拟磁盘分配给一个 iSCSI 目标。一旦虚拟磁盘被分配到某个目标，并且 iSCSI 启动器连接到该目标后，iSCSI 启动器就可以访问这个虚拟磁盘。所有被分配到同一个 iSCSI 目标的虚拟磁盘都可以被连接的 iSCSI 启动器访问。

## 示例

### 示例 1：将 VHD 关联到目标设备
```
PS C:\> Add-IscsiVirtualDiskTargetMapping -TargetName "TargetOne" -DevicePath "E:\Temp\vhd1.vhdx"
```

这个示例将 VHD 文件与路径 E:\Temp\vhd1.vhdx 关联到名为 “TargetOne” 的目标设备上。

### 示例 2：将 VHD 关联到目标设备，并设置 LUN
```
PS C:\> Add-IscsiVirtualDiskTargetMapping -TargetName "TargetOne" -DevicePath "E:\Temp\vhd1.vhdx" -Lun 0
```

这个示例将 VHD 文件与路径 “E:\Temp\vhd1.vhdx” 关联到名为 “TargetOne”的目标设备，并将 LUN 编号设置为 0。需要注意的是，每个目标的 LUN 编号必须是唯一的。

### 示例 3：将 RAM 磁盘与目标设备关联起来
```
PS C:\> Add-IscsiVirtualDiskTargetMapping -TargetName "TestTarget" -Path "ramdisk:test.vhdx"
```

这个示例将名为 “test” 的 RAM磁盘分配给目标对象 “TestTarget”。如果发起者连接到 “TestTarget”，它就可以访问该 RAM磁盘。

## 参数

### -ComputerName
如果此 cmdlet 在远程计算机上运行，则会指定该远程计算机的名称或 IP 地址。

如果此cmdlet在集群配置上运行，则指定集群资源组的网络名称或集群节点的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Credential
指定在连接到远程计算机时的凭据信息。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Lun
指定与虚拟磁盘相关联的逻辑单元号（LUN）。默认情况下，会分配最低可用的LUN编号。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定与iSCSI虚拟磁盘关联的虚拟硬盘（VHD）文件的路径。可以使用此参数来过滤iSCSI虚拟磁盘对象。

```yaml
Type: String
Parameter Sets: (All)
Aliases: DevicePath

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetName
指定 iSCSI 目标的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[Remove-IscsiVirtualDiskTargetMapping](./Remove-IscsiVirtualDiskTargetMapping.md)

